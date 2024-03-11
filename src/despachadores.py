import pulsar
from src.utils import *


class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        print('------------topico', topico)
        print('llego a publicar el mensaje')
        # json_schema = consultar_schema_registry(schema)
        # avro_schema = obtener_schema_avro_de_diccionario(json_schema)

        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        publicador = cliente.create_producer(topico)

        try:
            mensaje = "Hola, esto es un mensaje de ejemplo"
            publicador.send(mensaje.encode('utf-8'))
        except Exception as e:
            print("Error:", str(e))

        finally:
            publicador.close()
            cliente.close()
