from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from typing import Any
from Upscaler import upscale
import requests
from json import loads, dumps
import base64

app = Flask(__name__)


@app.route('/upscale_image', methods=['POST'])
def run_upscaler() -> Any:
    try:
        data = loads(request.get_json())
        if 'image_name' in data:

            image_name = data['image_name']

            url = "http://localhost:5003/get_image"  # todo: get rid of static url
            #print(23)
            json_data = dumps({"image_name": image_name})
            response = requests.post(url, json=json_data)
            response_data = response.json()
            #print(23)
            image_bytes = upscale(base64.b64decode(response_data["data"]["image"]), data["scale"])

            # Подготовка и отправка ответа
            if image_bytes:
                '''response_data = {
                    'response': 200,
                    'data': {
                        'image_name': data['scale'] + "Xupscaled_" + response_data["image_name"],
                        'image': base64.b64encode(image_bytes).decode('utf-8')
                    }
                }'''

                url = "http://localhost:5003/save_image"  # todo: get rid of static url

                response = requests.post(url, json=dumps(response_data))
                return jsonify({"response": response.status_code})
            else:
                return jsonify({'response': 404, 'error': 'Upscale failed.'}), 404
        else:
            return jsonify({'response': 400, 'error': 'Invalid request data'}), 400
    except Exception as e:
        print(e)
        return jsonify({'response': 500, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
