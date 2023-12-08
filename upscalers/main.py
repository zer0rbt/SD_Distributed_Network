import pika
import os
import sys
import json
from jsonschema import validate
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), "./../schemas/"))
from schemas.UpscalerSchema import Schema
from Controller import Controller


def main():
    ctrl = Controller()
    queue = "UPSCALER_QUEUE"

    def handler(
        chan: pika.channel.Channel,
        method: pika.spec.Basic.Deliver,
        props: pika.spec.BasicProperties,
        body: bytes,
    ):
        print(f"Recieved message from {os.getenv(queue)}")
        params = json.loads(body)
        validate(instance=params, schema=Schema)

        ctrl.handle(params)

    conn = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBIT_HOST"),
        )
    )
    chan = conn.channel()
    chan.queue_declare(os.getenv(queue))

    chan.basic_consume(
        queue=os.getenv(queue),
        auto_ack=True,
        on_message_callback=handler,
    )

    chan.start_consuming()


if __name__ == "__main__":
    load_dotenv(".env")
    main()
