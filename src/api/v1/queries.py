from .schemas import *


@strawberry.type
class Query:
    companies: typing.List[Company] = strawberry.field(resolver=get_companies)
