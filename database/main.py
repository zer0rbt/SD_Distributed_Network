from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from typing import Any
from db import get_image_from_db, save_image_to_db
from json import loads
import base64
import os

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test() -> Any:
    response_data = {
        "response": 200,
        "data": "test",
    }
    return jsonify(response_data), 200


@app.route("/save_image", methods=["POST"])
def save_image() -> Any:
    print(3)
    try:
        data = loads(request.get_json())  # Ожидаем входные данные в формате JSON
        print(5)
        print(list(data.keys()))
        if "image_name" in data["data"] and "image" in data["data"]:
            # Извлечение данных из запроса
            image_name = data["data"]["image_name"]
            image_bytes = base64.b64decode(data["data"]["image"])

            save_image_to_db(image_name=image_name, image_bytes=image_bytes)

            response_data = {"response": 200}
            return jsonify(response_data), 200
        else:
            return jsonify({"response": 400, "error": "Invalid request data"}), 400
    except Exception as e:
        print(e)
        return jsonify({"response": 500, "error": str(e)}), 500


@app.route("/get_image", methods=["POST"])
def get_image_and_send_response() -> Any:
    # print(4)
    try:
        data = loads(request.get_json())  # Ожидаем входные данные в формате JSON
        print(5)
        print(list(data.keys()))
        if "image_name" in data["data"]:
            image_name = data["data"]["image_name"]
            print(image_name)

            image_bytes = get_image_from_db(image_name)
            print(2)
            # Подготовка и отправка ответа
            if image_bytes:
                response_data = {
                    "response": 200,
                    "data": {
                        "image_name": image_name,
                        "image": base64.b64encode(image_bytes).decode("utf-8"),
                    },
                }
                print(3)
                return jsonify(response_data), 200
            else:
                return jsonify({"response": 404, "error": "Image not found"}), 404
        else:
            image_directory = os.getenv("IMAGES_PATH")

            if not os.path.exists(image_directory):
                os.makedirs(image_directory)

            image_path = os.path.join(image_directory, "error.txt")

            file = open(image_path, "w")
            file.write(str(request))
            file.close()
            return jsonify({"response": 400, "error": "Invalid request data"}), 400
    except Exception as e:
        print(request)
        return jsonify({"response": 500, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host=os.getenv("DATABASE_HOST"), port=os.getenv("DATABASE_PORT"))
