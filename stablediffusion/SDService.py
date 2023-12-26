import sdkit
from sdkit.models import load_model
from sdkit.generate import generate_images
from sdkit.utils import save_images
import os


class SDService:
    def __init__(self, model_path: str) -> None:
        self.model_name = "stable-diffusion"
        self.test_mode = False

        if os.getenv("TEST_MODE") == "YES":
            self.test_mode = True
            print("SDService init in test mode")
            return

        context = sdkit.Context()

        # set the path to the model file on the disk
        context.model_paths[self.model_name] = model_path
        load_model(context, self.model_name)

        self.sdkit_context = context

    def run(self, prompt: str) -> bytes:
        if self.test_mode == True:
            print("SDService run in test mode")
            return []

        # generate the image
        image = generate_images(
            self.sdkit_context,
            prompt=prompt,
            seed=420,
            width=512,
            height=512,
        )[0]

        image_directory = os.getenv("IMAGES_CACHE_PATH")

        if not os.path.exists(image_directory):
            os.makedirs(image_directory)

        image_path = os.path.join(image_directory, str(prompt) + ".png")
        save_images([image], ".")
        with open("image_0.jpeg", "rb") as f:
            return f.read()
