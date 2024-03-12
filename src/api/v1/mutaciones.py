import uuid
from strawberry.types import Info
from src.utils import *
from src.despachadores import Despachador
from .esquemas import *


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def crear_reserva(self, name: str, location: str, typeCompany: str, info: Info) -> CompanyRespuesta:
        payload = dict(
            name=name,
            location=location,
            typeCompany=typeCompany
        )
        comando = dict(
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
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-reserva",
                                                  "public/default/comando-crear-reserva")
        return CompanyRespuesta(mensaje="Procesando Mensaje", codigo=203)
