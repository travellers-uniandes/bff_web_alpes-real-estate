import time
import os
import datetime
import requests
import json
from fastavro.schema import parse_schema
from pulsar.schema import *

epoch = datetime.datetime.utcfromtimestamp(0)
PULSAR_ENV: str = 'BROKER_HOST'

def time_millis():
    return int(time.time() * 1000)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def millis_a_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)

def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")


def consultar_schema_registry(topico: str) -> dict:
    
  
    try:
      
        print('---------------------topico',topico)
        response = requests.get(f'http://{broker_host()}:6650/admin/v2/schemas/{topico}/schema')
        print('url----',f'http://{broker_host()}:6650/admin/v2/schemas/{topico}/schema')

        print('-------------response', response)
        if response.status_code != 200:
            print('-------------response', response.text)
        return {}
        # if response.status_code == 200:
        #     json_registry = response.json()
        #     return json.loads(json_registry.get('data', {}))
        # else:
        #     # Handle non-200 status codes here
        #     return {}  # or raise an exception
    except Exception as e:
        print('-----------error',str(e))
 

def obtener_schema_avro_de_diccionario(json_schema: dict) -> AvroSchema:
    definicion_schema = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=definicion_schema)

