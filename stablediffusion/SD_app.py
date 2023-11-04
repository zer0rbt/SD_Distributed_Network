from flask import Flask, request, jsonify
import requests
from typing import Any
from SD import make_image
from json import loads, dumps
import base64

app = Flask(__name__)


@app.route('/make_image', methods=['POST'])
def run_maker() -> Any:
    #print(1)
    try:
        data = loads(request.get_json())
        print(data)
        if "prompt" in data:
            prompt = data["prompt"]
            #print(4)
            image_bytes = make_image(prompt=prompt)
            #print(2)
            # Подготовка и отправка ответа
            if image_bytes:
                response_data = {
                    'response': 200,
                    'data': {
                        'image_name': prompt + ".png",
                        'image': base64.b64encode(image_bytes).decode('utf-8')
                    }
                }
                #print(3)
                url = "http://localhost:5003/save_image"  # todo: get rid from static url
                response_json = dumps(response_data)
                response = requests.post(url, json=response_json)
                #print(4)
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
