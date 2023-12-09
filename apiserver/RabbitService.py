import pika
import os
import json
from uuid import *


class RabbitService:
    def __init__(self) -> None:
        queue = os.getenv("STABLEDIFFUSION_QUEUE")

        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBIT_HOST"),
            )
        )

        self.chan = self.conn.channel()
        self.chan.queue_declare(queue)

    def send_generation_request(self, prompt: str) -> UUID:
        uuid = uuid4()

        message = {
            "prompt": prompt,
            "uuid": str(uuid),
        }

        self.chan.basic_publish(
            exchange="",
            routing_key=os.getenv("STABLEDIFFUSION_QUEUE"),
            body=json.dumps(message),
        )

        return uuid
