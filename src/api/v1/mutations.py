import uuid
import strawberry
from strawberry.types import Info
from src.utils import time_millis
from src.dispatchers import Dispatcher
from .schemas import ResponseCompany


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def crear_reserva(self, name: str, location: str, type_company: str, info: Info) -> ResponseCompany:
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
        dispatcher = Dispatcher()
        info.context["background_tasks"].add_task(dispatcher.post_message, command, "create-company",
                                                  "public/default/create-company")
        return ResponseCompany(message="Procesando Mensaje", code=203)
