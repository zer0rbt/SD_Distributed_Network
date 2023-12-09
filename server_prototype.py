import asyncio
import requests
from json import dumps
import io
from PIL import Image
import base64



async def init(script_path):
    process = await asyncio.create_subprocess_exec("python", script_path)
    await process.wait()



if __name__ == "__main__":
    """script_paths = ["./stablediffusion/SD_app.py", './database/db_app.py', "./upscalers/Upscaler.app"]
    for script_path in script_paths:
        asyncio.run(init(script_path))"""
    # {"uuid":"1112", "prompt":"anime girl, green hair, smile, white shirt, black baskeri"}

    prompt = "anime girl, green hair, smile, white shirt, black baskeri"
    url = "http://127.0.0.1:5001/make_image"
    json = dumps({'prompt': prompt})
    response = requests.post(url, json=json)
    url = "http://127.0.0.1:5002/upscale_image"
    json = dumps({"image_name": prompt + ".png", "scale":2})
    response = requests.post(url, json=json)


