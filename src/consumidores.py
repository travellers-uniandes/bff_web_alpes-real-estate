import logging
import traceback
import _pulsar
import aiopulsar
from src.utils import *


async def suscribirse_a_topico(topico: str, suscripcion: str, schema: str,
                               tipo_consumidor: _pulsar.ConsumerType = _pulsar.ConsumerType.Shared, eventos=[]):
    try:
        json_schema = consultar_schema_registry(schema)
        avro_schema = obtener_schema_avro_de_diccionario(json_schema)
        async with aiopulsar.connect(f'pulsar://{broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                    topico,
                    consumer_type=tipo_consumidor,
                    subscription_name=suscripcion,
                    schema=avro_schema
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)

    except:
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}, {schema}')
        traceback.print_exc()
