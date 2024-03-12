import typing
import strawberry
import requests
import os
from datetime import datetime

COMPANIES_HOST = os.getenv("COMPANIES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


def obtener_companies(root) -> typing.List["Company"]:
    companies_json = requests.get(f'http://{COMPANIES_HOST}:5000/company').json()
    companies = []

    for reserva in companies_json:
        companies.append(
            Company(
                fecha_creacion=datetime.strptime(reserva.get('fecha_creacion'), FORMATO_FECHA),
                fecha_actualizacion=datetime.strptime(reserva.get('fecha_actualizacion'), FORMATO_FECHA),
                id=reserva.get('id'),
                id_usuario=reserva.get('id_usuario', '')
            )
        )

    return companies


@strawberry.type
class Company:
    id: str
    name: str
    location: str
    typeCompany: str
    events: typing.List[str]
    createdAt: datetime
    updatedAt: datetime


@strawberry.type
class CompanyRespuesta:
    mensaje: str
    codigo: int
