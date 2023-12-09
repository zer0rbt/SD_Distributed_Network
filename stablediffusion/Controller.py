from PIL import Image
from uuid import uuid4, UUID
import os
import sys
import requests
from json import loads, dumps

sys.path.append(os.path.join(os.path.dirname(__file__), "./../utils/"))
from base64_coder import base64_to_binary, binary_to_base64
from SDService import SDService


class Controller:
    def __init__(self) -> None:
        self.sd_service: SDService = SDService(
            os.getenv("STABLEDIFFUSION_MODEL_PATH"),
        )

        self.images_cache = {}

    def dbfize_image(self, image_bytes: bytes, image_uuid: UUID):
        request_data = {
            "data": {
                "image_name": f"{image_uuid}.png",
                "image": binary_to_base64(image_bytes),
            },
        }
        db_host = os.getenv("DATABASE_HOST")
        db_port = os.getenv("DATABASE_PORT")
        response = requests.post(f"http://{db_host}:{db_port}/save_image", json=dumps(request_data))
        return response

    def handle(
        self,
        params: dict,
    ) -> UUID:
        prompt: str = params["prompt"]

        generated_image = self.sd_service.run(prompt)
        uuid: UUID = params["uuid"]
        self.dbfize_image(generated_image, uuid)

        return uuid


