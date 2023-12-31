import pika
import os
import sys
import json
from jsonschema import validate
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), "./../schemas/"))
from schemas.SDSchema import Schema

sys.path.append(os.path.join(os.path.dirname(__file__), "./../utils/"))
from utils.base64_coder import binary_to_base64
from Controller import Controller


def main():
    ctrl = Controller()
    queue = os.getenv("STABLEDIFFUSION_QUEUE")

    def handler(
        chan: pika.channel.Channel,
        method: pika.spec.Basic.Deliver,
        props: pika.spec.BasicProperties,
        body: bytes,
    ):
        params = json.loads(body)
        validate(instance=params, schema=Schema)

        uuid = ctrl.handle(params)


        message = {
            "uuid": uuid,
            "scale": 4,
        }

        chan.basic_publish(
            exchange="",
            routing_key=os.getenv("UPSCALER_QUEUE"),
            body=json.dumps(message),
        )

    conn = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBIT_HOST"),
        )
    )
    chan = conn.channel()
    chan.queue_declare(queue)

    chan.basic_consume(
        queue=queue,
        auto_ack=True,
        on_message_callback=handler,
    )

    chan.start_consuming()


if __name__ == "__main__":
    load_dotenv(".env")
    main()

