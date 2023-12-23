import json

database_path = "database.json"


def save_to_database(data):
    with open(database_path, "w") as f:
        json.dump(data, f)


def load_from_database():
    with open(database_path, "r") as f:
        return json.load(f)
