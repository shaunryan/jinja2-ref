import json
from genson import SchemaBuilder
import yaml
import os


def yaml_to_json(from_path:str, to_path:str):

    with open(from_path, "r") as file:
        data = yaml.safe_load(file)
    
    with open(to_path, "w") as file:
        data_json = json.dumps(data, indent=4)
        file.write(data_json)


def get_json_path(from_path:str, dest_dir:str):

    file, ext = os.path.splitext(from_path)
    filename = os.path.basename(file)
    path = f"{dest_dir}/{filename}.json"

    return path

def create_schema(form_path:str, dest_dir:str):


    builder = SchemaBuilder()
    with open(form_path, 'r') as f:
        datastore = json.load(f)
        builder.add_object(datastore )

    schema = builder.to_schema()

    schema_path = get_json_path(form_path, dest_dir)

    with open(schema_path, "w") as file:
        data_json = json.dumps(schema, indent=4)
        file.write(data_json)



for dirpath, dirnames, filenames in os.walk("./jinja2_ref/templates/jaffle_shop"):

    for f in filenames:

        form_path = f"{dirpath}/{f}"
        to_path = get_json_path(form_path, "./json")
        yaml_to_json(form_path, to_path)

for dirpath, dirnames, filenames in os.walk("./json"):
    for f in filenames:
        form_path = f"{dirpath}/{f}"
        create_schema(form_path, "./json_schema")


