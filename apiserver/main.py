from click import UUID
from flask import Flask, request, jsonify
from typing import Any
import os
from RabbitService import RabbitService
import requests

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
def mk_image() -> Any:
    print(-1)
    try:
        data = request.get_json()  # Ожидаем входные данные в формате JSON
        prompt = data.get("prompt")
        print(prompt)
        if prompt:
            uuid: UUID = rabbit.send_generation_request(prompt)
            print(2)
            response_data = {"response": 200, "data": {"uuid": str(uuid)}}
            return jsonify(response_data), 200
        else:
            return jsonify({"response": 400, "error": "Invalid request data"}), 400
    except Exception as e:
        print(request.data)
        return jsonify({"response": 500, "error": str(e)}), 501

@app.route("/get", methods=["POST"])
def retoute_get_image():
    db_host = os.getenv("DATABASE_HOST")
    db_port = os.getenv("DATABASE_PORT")
    response = requests.post(f"http://{db_host}:{db_port}/get_image", json=request.get_json())
    return response.json()

if __name__ == "__main__":
    app.run(host=os.getenv("APISERVER_HOST"), port=os.getenv("APISERVER_PORT"))
