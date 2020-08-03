from ariadne import MutationType, QueryType, gql, load_schema_from_path, make_executable_schema
from os.path import dirname, join

from doctors.resolvers.mutations.doctors import *
from doctors.resolvers.queries.doctors import *

def load_typedef_from_schema():
    type_def = load_schema_from_path(join(dirname(dirname(__file__)), "./gql"))
    type_defs = gql(type_def)
    return type_defs


# query type and its fields resolvers
def bind_query_type_to_resolvers():
    query = QueryType()
    query.set_field("doctor", DoctorsQueries.get_doctor)
    query.set_field("doctors", DoctorsQueries.get_doctors)
    return query