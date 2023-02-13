import os

import django
from django.conf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from strawberry.printer import print_schema
from strawberry.schema import BaseSchema
from strawberry.utils.importer import import_module_symbol

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup(set_prefix=False)

schema: BaseSchema = import_module_symbol("schema:schema")  # type: ignore

if settings.DEBUG:
    with open("schema.graphql", "w") as fp:
        print(print_schema(schema), file=fp)


app = FastAPI(debug=settings.DEBUG)

graphql_app = GraphQL(
    schema=schema,
    graphiql=settings.DEBUG,
    debug=settings.DEBUG,
    keep_alive=False,
    keep_alive_interval=10,
)

app.add_route("/", graphql_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
