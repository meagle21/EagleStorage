from flask import Flask, render_template, request
from aws import AWS
from system_tasks import System_Tasks
from tree import ParentNode, ChildNode

app = Flask(__name__)

### INITIALIZE OBJECTS TO USE CUSTOM METHODS
AWS_Class, System_Class = AWS(), System_Tasks()
s3_data = AWS_Class.get_all_objects()

### IN MAIN.PY COMPLETE THE FINAL DATA POINT COLLECTION 
parent_nodes = []
search_space = []
readable_search_space = []

for obj in s3_data[:]:
    if(obj['FileType'] == 'folder'):
        parent_node_as_object = ParentNode(obj)
        parent_nodes.append(parent_node_as_object)

for file in s3_data[:]:
    for parent_node in parent_nodes:
        if((file["ParentFolder"] == parent_node.get_node_name()[:-1]) and (file['FileType'] != 'folder')):
            parent_node.add_child(ChildNode(file))
            s3_data.remove(file)

for parent_node in parent_nodes[:]:
    for potential_parent_node in parent_nodes:
        if(parent_node.get_parent() == potential_parent_node.get_node_name()[:-1]):
            potential_parent_node.add_child(parent_node)
    if(len(parent_node.get_parent()) == 0):
        search_space.append(parent_node)
        readable_search_space.append(parent_node.get_node_name())

@app.route('/', methods = ['GET'])
def home():
    file_data = [[data.get_node_name(), System_Class.get_icon_path(data.get_file_type()), data.get_num_children()] for data in search_space]
    return render_template("index.html", file_info = file_data)

@app.route('/<folder>', methods = ['POST', 'GET'])
def file_tree_traversal(folder):
    for parent_node in parent_nodes:
        if(parent_node.get_node_name()[:-1] == folder):
            file_data = [[data.get_node_name(), System_Class.get_icon_path(data.get_file_type()), data.get_num_children()] for data in parent_node.get_children()]
    return render_template("index.html", file_info = file_data)