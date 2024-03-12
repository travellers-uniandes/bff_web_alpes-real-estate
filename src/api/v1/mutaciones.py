import uuid
from strawberry.types import Info
from src.utils import time_millis
from src.despachadores import Despachador
from .esquemas import *


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def crear_reserva(self, name: str, location: str, type_company: str, info: Info) -> CompanyRespuesta:
        payload = dict(
            name=name,
            location=location,
            typeCompany=type_company
        )
        command = dict(
            id=str(uuid.uuid4()),
            time=time_millis(),
            specversion="v1",
            type="ComandoReserva",
            ingestion=time_millis(),
            datacontenttype="AVRO",
            service_name="BFF Web",
            data=payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.post_message, command, "comando-crear-reserva",
                                                  "public/default/comando-crear-reserva")
        return CompanyRespuesta(mensaje="Procesando Mensaje", codigo=203)
