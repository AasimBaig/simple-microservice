import json
from ariadne.asgi import GraphQL
from ariadne import QueryType, gql, make_executable_schema

with open('./data.json', 'r') as f:
    data = json.load(f)

type_defs = gql("""
    type Query {
        allCheck: Boolean
        allCollections: [Collections]
    }

    type Collections{
        title: String
        verified: Boolean
        image: String
        snippets: [Int]
    }

""")

# Create type instance for Query type defined in our schema...
query = QueryType()

# ...and assign our resolver function to its query field.
@query.field("allCheck")
def resolve_all_check(_, info):
    return True


@query.field("allCollections")
def resolve_all_collections(_, info):
    return get_collections()


def get_collections():
    return data["collections"]

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)