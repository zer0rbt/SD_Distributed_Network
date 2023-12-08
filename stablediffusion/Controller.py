from PIL import Image
from uuid import uuid4, UUID
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./../utils/"))
from base64_coder import base64_to_binary
from SDService import SDService


class Controller:
    def __init__(self) -> None:
        self.sd_service: SDService = SDService(
            os.getenv("STABLEDIFFUSION_MODEL_PATH"),
        )

        self.images_cache = {}

    def cache_image(self, image_bytes: bytes) -> UUID:
        image_uuid = uuid4()

        file_path = os.path.join(
            os.getenv("IMAGES_CACHE_PATH"),
            f"{image_uuid}.png",
        )
        image_file = open(
            file_path,
            "wb",
        )
        image_file.write(image_bytes)
        image_file.close()

        self.images_cache[image_uuid] = file_path

        return image_uuid

    def handle(
        self,
        params: dict,
    ) -> UUID:
        prompt: str = params["prompt"]

        generated_image = self.sd_service.run(prompt)
        uuid: UUID = self.cache_image(generated_image)

        self.send_image_to_cdn(uuid, generated_image)

        return uuid

    def send_image_to_cdn(
        self,
        uuid: UUID,
        image_bytes: bytes,
    ):
        pass
