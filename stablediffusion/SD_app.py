from flask import Flask, request, jsonify
import requests
from typing import Any
from SD import make_image
from json import loads, dumps
import base64

app = Flask(__name__)


@app.route('/make_image', methods=['POST'])
def run_maker() -> Any:
    """
    Function, that gets http requests and starting image generation.

    Receives json-request of following format:
        {"generation_data":dict, "save_url":str},
    where "generation_data" key contains data generation information, and "save_url" contains url, where located db.

    dev note: for simplicity, you can use {"prompt": "place_any_string"} as "generation_data".

    :return: Json file with 'response' key and 'error' key (optional)
    """
    # print(1)
    try:
        data = loads(request.get_json())
        print(data)
        if "generation_data" in data and "prompt" in data["generation_data"] and "save_url" in data:
            gen_data = data["generation_data"]
            # print(4)
            image_bytes = make_image(gen_data)
            # print(2)
            # Подготовка и отправка ответа
            if image_bytes:
                response_data = {
                    'response': 200,
                    'data': {
                        'image_name': data["generation_data"]["prompt"] + ".png",
                        'image': base64.b64encode(image_bytes).decode('utf-8')
                    }
                }
                response_json = dumps(response_data)
                response = requests.post(data["save_url"], json=response_json)
                return jsonify({"response": response.status_code})
            else:
                return jsonify({'response': 404, 'error': 'Generation failed.'}), 404
        else:
            return jsonify({'response': 400, 'error': 'Invalid request data'}), 400
    except Exception as e:
        print(e)
        return jsonify({'response': 500, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
