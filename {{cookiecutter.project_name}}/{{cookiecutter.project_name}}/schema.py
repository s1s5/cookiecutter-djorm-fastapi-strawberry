import strawberry


@strawberry.federation.type(extend=True)
class Query:
    @strawberry.field
    async def {{cookiecutter.project_name}}_version(self) -> str:
        return "v0.0.0"


@strawberry.federation.type(extend=True)
class Mutation:
    @strawberry.field
    async def {{cookiecutter.project_name}}_test_mutation(self) -> str:
        return "hello world"
