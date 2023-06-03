from rdflib import Graph, Namespace

ontology_file = "C://Users//admin//ontologyPython//Final.owl"

g = Graph()
g.parse(ontology_file)  #, format="xml"

namespace = Namespace("http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#")

# Query for all fields and their description data properties
query = """
    SELECT ?field_label ?description
    WHERE {{
        ?field rdf:type my_ns:Field .
        ?field rdfs:label ?field_label .
        ?field my_ns:Description ?description .
    }}
"""

results = g.query(query, initNs={"my_ns": namespace, "rdfs": "http://www.w3.org/2000/01/rdf-schema#"})

# Print each field label and its description data property
for row in results:
    field_label = row.field_label
    description = row.description
    print(f"{field_label}")
    print(f"{description}")
    print()

namespace = Namespace("http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#")

query = """
    SELECT ?button_label ?description
    WHERE {{
        ?button rdf:type my_ns:Button .
        ?button rdfs:label ?button_label .
        ?button my_ns:Description ?description .
    }}
"""

results = g.query(query, initNs={"my_ns": namespace, "rdfs": "http://www.w3.org/2000/01/rdf-schema#"})

# Print each button label and its description data property
for row in results:
    button_label = row.button_label
    description = row.description
    print(f"{button_label}")
    print(f"{description}")
    print()