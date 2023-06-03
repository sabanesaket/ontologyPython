from rdflib import Graph, RDF, RDFS, URIRef, Namespace
from rdflib.plugins.sparql import prepareQuery

# Load the ontology from a file or URL
ontology_file = "C://Users//admin//ontologyPython//Final.owl"

g = Graph()
g.parse(ontology_file)  #, format="xml"

# Define the namespace prefix used in the ontology
namespace = {
    "ont": "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#"
}

# Define the specific instance URI for which you want to retrieve the results
instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Check-out"

# Query for the specific instance and retrieve its concept property and label
query = """
    SELECT ?concept ?label
    WHERE {{
        <{instance_uri}> rdf:type ont:screen .
        <{instance_uri}> ont:Concept ?concept .
        <{instance_uri}> rdfs:label ?label .
    }}
""".format(instance_uri=instance_uri)

results = g.query(query, initNs=namespace)

# Print the concept property and label for the specific instance
for result in results:
    concept = result.concept
    label = result.label
    print(label + "\n")
    print(concept + "\n")
    
query1 = """
SELECT ?TaskDesc
WHERE {{
    <{instance_uri}> ont:TaskDesc ?TaskDesc .
}}
""".format(instance_uri=instance_uri)

results = g.query(query1, initNs=namespace)

for result in results:
    task_desc = result.TaskDesc
    print(task_desc + "\n")

# Define the specific instance URI for which you want to retrieve the results
instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Check-out"

# Query for retrieving the range of fields with object property isFieldOn having value 'Check-out'
query = """
    SELECT ?field ?range
    WHERE {{
        ?field rdf:type ont:field .
        ?field ont:isFieldOn <{instance_uri}> .
        ?field rdfs:range ?range .
    }}
""".format(instance_uri="http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Check-out")

results = g.query(query, initNs=namespace)
# print(results)

# Print the retrieved fields and their associated ranges
for result in results:
    field = result.field
    range_value = result.range
    print("Field:", field)
    print("Range:", range_value)
    print()


# query = 'SELECT ?field ?action WHERE { ?field :isFieldOn {instance_uri} }'
# query = """
#     PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Check-out>
#     SELECT ?field ?action
#     WHERE {
#         my_ns:Check-out my_ns:hasField ?field .
#     }
# """

query = """
    PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
    SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o .
        FILTER (?s = my_ns:Check-out && ?p = my_ns:hasField)
    }
"""

# my_ns = Namespace("http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#")
# g.bind("my_ns",my_ns)
# prepared_query = prepareQuery(query)
# results = g.query(prepared_query)

results = g.query(query)
# print(len(results))
# print("Got Results")


# results = g.query(query, initNs=namespace)

# print()
# print()
# print()
# print("Printing Results")
# print(results)
count = 1
for row in results:
    s = row.s
    p = row.p
    o = row.o
    # print(o.Action)
    # print(f"Subject: {s}, Predicate: {p}, Object: {o}")
    data_query = f"""
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?dpo
        WHERE {{
            <{o}> my_ns:Action ?dpo .
        }}
    """

    data_results = g.query(data_query)
    

    for data_row in data_results:
        # dp = data_row.dp
        dpo = data_row.dpo
        print(f"{count}.{dpo}")
    count+=1

query = """
    PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
    SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o .
        FILTER (?s = my_ns:Search_catalogue && ?p = my_ns:hasButton)
    }
"""
results = g.query(query)
for row in results:
    s = row.s
    p = row.p
    o = row.o
    # print(o.Action)
    # print(f"Subject: {s}, Predicate: {p}, Object: {o}")
    data_query = f"""
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?dpo
        WHERE {{
            <{o}> my_ns:Action ?dpo .
        }}
    """

    data_results = g.query(data_query)
    

    for data_row in data_results:
        # dp = data_row.dp
        dpo = data_row.dpo
        print(f"{count}.{dpo}")
    count+=1

print()

# print(g.serialize(format="turtle"))