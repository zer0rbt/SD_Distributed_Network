from PIL import Image
from uuid import uuid4, UUID
import os
import sys
import requests
from json import loads, dumps

sys.path.append(os.path.join(os.path.dirname(__file__), "./../utils/"))
from base64_coder import base64_to_binary, binary_to_base64
from UpscalerService import UpscalerService


class Controller:
    def __init__(self) -> None:
        self.upscaler_service: UpscalerService = UpscalerService(
            os.getenv("UPSCALER_MODEL_PATH"),
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
        return image_uuid

    def undbfize_image(self, image_uuid: UUID) -> str:
        request_data = {
            "data": {
                "image_name": f"{image_uuid}.png",
            },
        }
        db_host = os.getenv("DATABASE_HOST")
        db_port = os.getenv("DATABASE_PORT")
        response = requests.post(f"http://{db_host}:{db_port}/get_image", json=dumps(request_data)).json()
        return image_uuid

    def handle(
        self,
        params: dict,
    ) -> UUID:
        input_image_bytes: str = self.undbfize_image(params["uuid"])
        scale: int = params["scale"]

        upscaled_image = self.upscaler_service.run(base64_to_binary(input_image_bytes), scale)
        uuid: UUID = self.dbfize_image(upscaled_image, params["uuid"])

        return uuid

