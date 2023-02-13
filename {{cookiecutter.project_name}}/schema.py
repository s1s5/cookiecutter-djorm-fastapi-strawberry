import strawberry

from {{cookiecutter.project_name}} import schema as {{cookiecutter.project_name}}_schema


schema = strawberry.federation.Schema(
    query={{cookiecutter.project_name}}_schema.Query,
    mutation={{cookiecutter.project_name}}_schema.Mutation,
    enable_federation_2=True
)
