from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import owlready2
from owlready2 import ThingClass
from rdflib import Graph, RDF, RDFS, URIRef, Namespace
from rdflib.plugins.sparql import prepareQuery

ontology_file = "Final.owl"
g = Graph()
g.parse(ontology_file)


def FAQ(request):
    # Import the OWL ontology file.
    ontology = owlready2.get_ontology("Final.owl").load()
    # Parse the OWL ontology file.
    classes = ontology.classes()
    classesList = list(classes)
    FAQClass = classesList[2]
    instances = FAQClass.instances()
    mydict = {}
    for i in range(len(instances)):
        for j in range(len(instances[i].Question)):
            mydict[instances[i].Question[j]] = instances[i].Answer[j]
    params = {'data':mydict}
    return render(request,'ontologytest1/faq.html',params)

def index(request):
    return render(request,'ontologytest1/basic.html')

def about(request):
    return render(request, 'about.html')

def add_a_book(request):
    # Define the namespace prefix used in the ontology
    namespace = {
        "ont": "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#"
    }
    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Add_a_book"
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
    conceptList = []
    labelList = []
    for result in results:
        concept = result.concept
        conceptList.append(str(concept))
        label = result.label
        labelList.append(str(label))
    concept = conceptList[0]
    label = labelList[0]
        
    query1 = """
    SELECT ?TaskDesc
    WHERE {{
        <{instance_uri}> ont:TaskDesc ?TaskDesc .
    }}
    """.format(instance_uri=instance_uri)

    results = g.query(query1, initNs=namespace)

    task_desc_List = []
    for result in results:
        task_desc = result.TaskDesc
        task_desc_List.append(task_desc)
    task_desc = task_desc_List[0]

    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Add_a_book"

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Add_a_book && ?p = my_ns:hasField)
        }
    """
    results = g.query(query)

    count = 1
    tasksList = []
    for row in results:
        s = row.s
        p = row.p
        o = row.o
        data_query = f"""
            PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
            SELECT ?dpo
            WHERE {{
                <{o}> my_ns:Action ?dpo .
            }}
        """
        data_results = g.query(data_query)
        for data_row in data_results:
            dpo = data_row.dpo
            tasksList.append(str(dpo))
        count+=1

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Add_a_book && ?p = my_ns:hasButton)
        }
    """
    tasksButtons = []
    results = g.query(query)
    for row in results:
        s = row.s
        p = row.p
        o = row.o
        data_query = f"""
            PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
            SELECT ?dpo
            WHERE {{
                <{o}> my_ns:Action ?dpo .
            }}
        """
        data_results = g.query(data_query)
        for data_row in data_results:
            dpo = data_row.dpo
            tasksButtons.append(str(dpo))
        count+=1

    resultDict = {'concept':concept, 'label':label, 'task_desc':task_desc, 'tasks':tasksList, 'tasksButtons':tasksButtons}
    return render(request, 'ontologytest1/add_a_book.html',{'data':resultDict})

def add_a_member(request):
    namespace = {
    "ont": "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#"
    }
    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Add_a_member"
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
    conceptList = []
    labelList = []
    for result in results:
        concept = result.concept
        conceptList.append(str(concept))
        label = result.label
        labelList.append(str(label))
    concet = conceptList[0]
    label = labelList[0]
    query1 = """
    SELECT ?TaskDesc
    WHERE {{
        <{instance_uri}> ont:TaskDesc ?TaskDesc .
    }}
    """.format(instance_uri=instance_uri)
    results = g.query(query1, initNs=namespace)
    task_desc_list = []
    for result in results:
        task_desc = result.TaskDesc
        task_desc_list.append(str(task_desc))
        print(task_desc + "\n")
    task_desc = task_desc_list[0]
    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Add_a_member"

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Add_a_member && ?p = my_ns:hasField)
        }
    """

    results = g.query(query)
    count = 1
    tasksList = []
    for row in results:
        s = row.s
        p = row.p
        o = row.o
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
            tasksList.append(str(dpo))
            # print(f"{count}.{dpo}")
        count+=1
    # print(tasksList)

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Add_a_member && ?p = my_ns:hasButton)
        }
    """
    results = g.query(query)
    tasksButtons = []
    for row in results:
        s = row.s
        p = row.p
        o = row.o
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
            tasksButtons.append(str(dpo))
            # print(f"{count}.{dpo}")
        count+=1
    resultDict = {'concept':concept, 'label':label, 'task_desc':task_desc, 'tasks':tasksList, 'tasksButtons':tasksButtons}
    return render(request,'ontologytest1/add_a_member.html',{'data':resultDict})

def check_out(request):
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
    conceptList = []
    labelList = []
    for result in results:
        concept = result.concept
        conceptList.append(str(concept))
        label = result.label
        labelList.append(str(label))
    concept = conceptList[0]
    label = labelList[0]
        
    query1 = """
    SELECT ?TaskDesc
    WHERE {{
        <{instance_uri}> ont:TaskDesc ?TaskDesc .
    }}
    """.format(instance_uri=instance_uri)

    results = g.query(query1, initNs=namespace)
    task_desc_list = []
    for result in results:
        task_desc = result.TaskDesc
        task_desc_list.append(str(task_desc))
        # print(task_desc + "\n")
    task_desc = task_desc_list[0]

    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Check-out"

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Check-out && ?p = my_ns:hasField)
        }
    """

    results = g.query(query)
    tasksList = []
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
            tasksList.append(str(dpo))
            # print(f"{count}.{dpo}")/
        count+=1
    # print(tasksList)

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Search_catalogue && ?p = my_ns:hasButton)
        }
    """
    tasksButtons = []
    results = g.query(query)
    for row in results:
        s = row.s
        p = row.p
        o = row.o
        data_query = f"""
            PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
            SELECT ?dpo
            WHERE {{
                <{o}> my_ns:Action ?dpo .
            }}
        """
        data_results = g.query(data_query)
        for data_row in data_results:
            dpo = data_row.dpo
            tasksButtons.append(str(dpo))
        count+=1
    resultDict = {'concept':concept, 'label':label, 'task_desc':task_desc, 'tasks':tasksList, 'tasksButtons':tasksButtons}
    return render(request, 'ontologytest1/check_out.html',{'data':resultDict})

def glossary(request):
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
    field_label_list = []
    description_list = []
    for row in results:
        field_label = row.field_label
        field_label_list.append(str(field_label).capitalize)
        description = row.description
        description_list.append(str(description))
    
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

    button_label_list = []
    description_list_1 = []
    # Print each button label and its description data property
    for row in results:
        button_label = row.button_label
        button_label_list.append(str(button_label))
        description = row.description
        description_list_1.append(str(description))

    field_label_description_list = list(zip(field_label_list,description_list))
    button_label_description_list = list(zip(button_label_list,description_list_1))

    
    resultDict = {'field_label_description_list':field_label_description_list, 'button_label_description_list':button_label_description_list}
    return render(request,'ontologytest1/glossary.html', {'data':resultDict})

def search_catalog(request):
    namespace = {
    "ont": "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#"
    }

    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Search_catalogue"

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
    conceptList = []
    labelList = []
    for result in results:
        concept = result.concept
        conceptList.append(str(concept))
        label = result.label
        labelList.append(str(label))
        
    query1 = """
    SELECT ?TaskDesc
    WHERE {{
        <{instance_uri}> ont:TaskDesc ?TaskDesc .
    }}
    """.format(instance_uri=instance_uri)

    results = g.query(query1, initNs=namespace)

    task_desc_list = []
    for result in results:
        task_desc = result.TaskDesc
        task_desc_list.append(str(task_desc))
        print(task_desc + "\n")
    print(task_desc_list)
    # task_desc = task_desc_list[0]
    

    # Define the specific instance URI for which you want to retrieve the results
    instance_uri = "http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#Search_catalogue"

    query = """
        PREFIX my_ns: <http://www.semanticweb.org/anant.sabane01/ontologies/2020/1/untitled-ontology-7#>
        SELECT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
            FILTER (?s = my_ns:Search_catalogue && ?p = my_ns:hasField)
        }
    """
    results = g.query(query)
    count = 1
    tasksList = []
    for row in results:
        s = row.s
        p = row.p
        o = row.o
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
            tasksList.append(str(dpo))
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
    tasksButtons = []
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
            tasksButtons.append(str(dpo))
            print(f"{count}.{dpo}")
        count+=1
    resultDict = {'concept':concept, 'label':label, 'tasks':tasksList, 'tasksButtons':tasksButtons} #'task_desc':task_desc,
    return render(request,'ontologytest1/search_catalog.html', {'data':resultDict}) 