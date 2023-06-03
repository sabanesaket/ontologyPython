from rdflib import Graph

g = Graph()

query = """
    PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7>
    SELECT ?field ?action
    WHERE {
        ?field my_ns:isFieldOn my_ns:Add_a_book .
    }
"""

results = g.query(query)
print(len(results))
print("Got Results")

for row in results:
    field = row.field
    action = row.action
    print(f"Field: {field}, Action: {action}")
