from PIL import Image

import sdkit
from sdkit.filter import apply_filters
from sdkit.models import load_model
import io
import os


class UpscalerService:
    def __init__(self, model_path: str) -> None:
        self.model_name = "realesrgan"

        if os.getenv("TEST_MODE") == "YES":
            self.test_mode = True
            print("UpscalerService init in test mode")
            return

        context = sdkit.Context()

        # set the path to the model file on the disk
        context.model_paths[self.model_name] = model_path
        load_model(context, self.model_name)

        self.sdkit_context = context

    def run(self, image_bytes: bytes, scale: int = 4) -> bytes:
        if self.test_mode == True:
            print("UpscalerService run in test mode")
            return image_bytes

        # apply the filter
        image_upscaled = apply_filters(
            self.sdkit_context,
            self.model_name,
            Image.open(io.BytesIO(image_bytes)),
            scale=scale,
        )[0]

        return image_upscaled.tobytes()
