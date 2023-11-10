import base64
from json import loads, dumps
from typing import Any

import requests
from flask import Flask, request, jsonify

from Upscaler import upscale

app = Flask(__name__)


@app.route('/upscale_image', methods=['POST'])
def run_upscaler() -> Any:
    """
        Function, that gets http requests and starts image upscaling.

        Receives json-request of following format:
            {"image_name":str, "get_url": str, "save_url":str},
        where:
         "image_name" contains image name.
         "get_url" contains a link to the database from which the photo will be taken.
         "save_url" contains an url to the database where the image will be saved.


        :return: Json file with 'response' key and 'error' key (optional)
        """
    try:
        data = loads(request.get_json())
        if 'image_name' in data:

            image_name = data['image_name']

            url = data["get_url"]
            json_data = dumps({"image_name": image_name})
            response = requests.post(url, json=json_data)
            response_data = response.json()
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

                url = data["save_url"]

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
