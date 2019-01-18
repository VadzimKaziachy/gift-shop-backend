import graphene
import presents.schema


class Query(presents.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
