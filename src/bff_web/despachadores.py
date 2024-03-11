import pulsar
from pulsar.schema import *

import utils

class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        print('------------topico',topico)
        print('llego a publicar el mensaje')
        # json_schema = utils.consultar_schema_registry(schema)  
        # avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        publicador.send(mensaje)
        cliente.close()
