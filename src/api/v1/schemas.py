import typing
import strawberry
import requests
import os
from datetime import datetime

COMPANIES_HOST = os.getenv("COMPANIES_ADDRESS", default="localhost")
FORMATO_FECHA = '%a, %d %b %Y %H:%M:%S GMT'


def get_companies(root) -> typing.List["Company"]:
    companies_json = requests.get('http://localhost:5001/company_router/company').json()
    companies = []
    for reserva in companies_json:
        created_at = datetime.strptime(reserva.get('createdAt'), FORMATO_FECHA)
        updated_at = datetime.strptime(reserva.get('updatedAt'), FORMATO_FECHA)
        companies.append(
            Company(
                updatedAt=updated_at,
                createdAt=created_at,
                id=reserva.get('id'),
                typeCompany=reserva.get('typeCompany'),
                name=reserva.get('name'),
                location=reserva.get('location'),
                events=reserva.get('events')
            )
        )
    return companies


@strawberry.type
class Company:
    id: str
    name: str
    location: str
    type_company: str
    events: typing.List[str]
    created_at: datetime
    updated_at: datetime


@strawberry.type
class ResponseCompany:
    message: str
    code: int
