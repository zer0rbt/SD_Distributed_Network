from click import UUID
from flask import Flask, request, jsonify
from typing import Any
import os
from RabbitService import RabbitService

app = Flask(__name__)
rabbit = RabbitService()


@app.route("/test", methods=["GET"])
def test() -> Any:
    response_data = {
        "response": 200,
        "data": "api test",
    }
    return jsonify(response_data), 200


@app.route("/generate", methods=["POST"])
def save_image() -> Any:
    try:
        data = request.get_json()  # Ожидаем входные данные в формате JSON
        prompt = data.get("prompt")

        if prompt:
            uuid: UUID = rabbit.send_generation_request(prompt)

            response_data = {"response": 200, "data": {"uuid": str(uuid)}}
            return jsonify(response_data), 200
        else:
            return jsonify({"response": 400, "error": "Invalid request data"}), 400
    except Exception as e:
        print(request.data)
        return jsonify({"response": 500, "error": str(e), "request": request.data}), 500


if __name__ == "__main__":
    app.run(host=os.getenv("APISERVER_HOST"), port=os.getenv("APISERVER_PORT"))
