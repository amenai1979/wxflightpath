from wxflightpath import config
import os
import sys
import shelve
import json

current_path=os.getcwd()
sys.path.append(current_path)
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_path)
def dumpdb():
    with shelve.open(config['DATA']['TRANSLATOR_DB']) as db:
        # Create a dictionary from the shelve items
        data_to_dump = dict(db.items())
        # Specify the output JSON file path
        json_file_path = config['DATA']['TRANSLATOR_DB_JSON']
        # Write the dictionary to a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(data_to_dump, json_file, indent=2, sort_keys=True)
        print(f"Data dumped to {json_file_path}")


def loaddb():
    # Specify the input JSON file path
    json_file_path = config['DATA']['TRANSLATOR_DB_JSON']

    # Read data from the JSON file
    with open(json_file_path, 'r') as json_file:
        data_to_load = json.load(json_file)

    # Open the shelve database
    with shelve.open(config['DATA']['TRANSLATOR_DB']) as db:
        # Update the shelve database with the loaded data
        db.update(data_to_load)


if __name__ == '__main__':
    dumpdb()