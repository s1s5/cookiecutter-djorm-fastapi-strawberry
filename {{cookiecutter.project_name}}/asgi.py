import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from strawberry.utils.importer import import_module_symbol
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup(set_prefix=False)


app = FastAPI(debug=settings.DEBUG)

graphql_app = GraphQL(
    schema=import_module_symbol("schema:schema"),
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
