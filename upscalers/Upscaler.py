from PIL import Image

import sdkit
from sdkit.filter import apply_filters
from sdkit.models import load_model
import os.path
import io
def upscale(image_bytes: bytes, scale: int = 4) -> bytes:
    """
    Function that upscales image.

    Requires "RealESRGAN_x4plus.pth" in the right place to work.

    :param image_bytes: image to upscale converted to data type "Bytes".
    :param scale: by what factor the new image will be larger than the original.
    :return:
    """
    context = sdkit.Context()

    # set the path to the model file on the disk
    context.model_paths["realesrgan"] = "C://SD//models//realesrgan//RealESRGAN_x4plus.pth"
    load_model(context, "realesrgan")

    # apply the filter
    image_upscaled = apply_filters(context, "realesrgan", Image.open(io.BytesIO(image_bytes)), scale=scale)[0]
    return image_upscaled