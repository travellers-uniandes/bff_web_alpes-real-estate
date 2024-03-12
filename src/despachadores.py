import json
import pulsar
from src.utils import broker_host


class Despachador:
    def __init__(self):
        ...

    @staticmethod
    async def post_message(message, topic, schema):
        client = pulsar.Client(f'pulsar://{broker_host()}:6650')
        producer = client.create_producer(topic)

        try:
            client = pulsar.Client(f'pulsar://{broker_host()}:6650')
            producer = client.create_producer(topic)
            data = message['data']
            serialized_data = json.dumps(data).encode('utf-8')
            producer.send(serialized_data)
        except Exception as e:
            print("Error:", str(e))

        finally:
            producer.close()
            client.close()
