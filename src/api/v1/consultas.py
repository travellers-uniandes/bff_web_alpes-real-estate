from .esquemas import *


@strawberry.type
class Query:
    companies: typing.List[Company] = strawberry.field(resolver=obtener_companies)
