from rdflib import Graph, RDF, RDFS, URIRef

from owlready2 import *

# Load the ontology
onto = get_ontology("C://Users//admin//ontologyPython//Final.owl").load()

# Get the screen instance
screen = onto.search_one(iri="*Add_a_book*")

# Iterate over the fields of the screen
for field in screen.hasField:
    #print("Field:")
    #print("Label:", field.rdfs.label[0])
    #print("Concept:", field.has_concept[0].concept_text)
    #print("Task Description:", field.has_task_description[0].task_description_text)
    print("Action:", field.has_action[0].action_text)
    print()

# Iterate over the buttons of the screen
for button in screen.hasButton:
    #print("Button:")
    #print("Label:", button.rdfs.label[0])
    #print("Concept:", button.has_concept[0].concept_text)
    #print("Task Description:", button.has_task_description[0].task_description_text)
    print("Action:", button.has_action[0].action_text)
    print()

# Define the specific instance URI for which you want to retrieve the results
instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Add_a_book"

# Query for the fields where isFieldOn matches 'Add a book' and retrieve their action
query = """
    SELECT ?field ?action
    WHERE {{
        ?field rdf:type ont:field .
        ?field ont:isFieldOn <{instance_uri}> .
        ?field ont:hasAction ?action .
    }}
""".format(instance_uri=instance_uri)

results = g.query(query, initNs=namespace)

# Print the field and its associated action
for result in results:
    action = result.action
    print("Field:", field)
    print("Action:", action)