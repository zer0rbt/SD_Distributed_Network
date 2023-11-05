import sdkit
from sdkit.models import load_model
from sdkit.generate import generate_images
from sdkit.utils import log



def make_image(data: dict) -> bytes:
    """
    Function that generates image for you. Requires specific model at the right path.

    :param data: dict with the keys from generate_images() args.
    :return: Photo decoded to bytes.
    """

    context = sdkit.Context()

    # Frodo: You can place path to any other model (if u have it ofc)
    context.model_paths['stable-diffusion'] = 'C://SD//models//stable-diffusion//wintermoonmix_A.safetensors'
    load_model(context, 'stable-diffusion')

    # generate the image
    images = generate_images(context, **data)

    # save the image
    return images[0].tobytes()
