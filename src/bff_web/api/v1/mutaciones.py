import strawberry
import typing

from strawberry.types import Info
import utils
from despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    # TODO Agregue objeto de itinerarios o reserva
    @strawberry.mutation
    async def crear_reserva(self, name: str, location: str, typeCompany: str, info:Info) -> CompanyRespuesta:
       
        payload = dict(
            name = name,
            location = location,
            typeCompany =typeCompany
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-reserva", "public/default/comando-crear-reserva")
        # info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-create-company1", "public/default/comando-create-company1")
        
        return CompanyRespuesta(mensaje="Procesando Mensaje", codigo=203)