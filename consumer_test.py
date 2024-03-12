from pulsar import ConsumerType, Client

pulsar_url = "pulsar://localhost:6650"
topic_name = "persistent://public/default/create-company"
subscription_name = "bff-sub-events"

client = Client(pulsar_url)
consumer = client.subscribe(
    topic_name,
    subscription_name,
    consumer_type=ConsumerType.Shared
)

try:
    while True:
        msg = consumer.receive()
        try:
            print("Mensaje recibido: {}".format(msg.data().decode('utf-8')))
        except Exception as e:
            print("Error al procesar el mensaje:", str(e))
        finally:
            consumer.acknowledge(msg)
except Exception as e:
    print("Error:", str(e))

finally:
    consumer.close()
    client.close()
