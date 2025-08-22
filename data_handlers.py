import json

# TODO: Create file handler for JSON (COMPLETE)
def get_json_data(json_file):
    with open(file=json_file, mode='r') as file:
        data = json.load(fp=file)
    return data


# TODO: Create a file handler for CSV - Consider Pandas or CSV lib (INCOMPLETE)
# TODO: Create a file handler for SQL (INCOMPLETE)