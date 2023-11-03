import sdkit
from sdkit.models import load_model
from sdkit.generate import generate_images
from sdkit.utils import log


def make_image(prompt: str):
    context = sdkit.Context()

    # Frodo: You can place path to any other model (if u have on ofc)
    context.model_paths['stable-diffusion'] = 'C://SD//models//stable-diffusion//wintermoonmix_A.safetensors'
    load_model(context, 'stable-diffusion')

    # generate the image
    images = generate_images(context, prompt=prompt, seed=420, width=512,
                             height=512)

    # save the image
    return images[0]
