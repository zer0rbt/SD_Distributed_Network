from stablediffusion.SD import make_image
from upscalers.Upscaler import upscale

if __name__ == "__main__":
    # Note: it won't work if you do not have SD model, sdkit library & upscaler pre-installed
    img = make_image('anime girl, green hair, opened mouth, white clothes')
    img.save("img.png")
    img = upscale(img)
    img.save("img_ups.png")
