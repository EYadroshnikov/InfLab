import json_service as json_service


def sellers_get_all():
    db = json_service.load_from_database()
    return db["sellers"]


def sellers_get_one_by_name(name):
    db = json_service.load_from_database()
    for elem in db["sellers"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


def sellers_update_one_by_id(id, seller):
    db = json_service.load_from_database()
    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:
            elem["name"] = seller["name"]
            elem["shop_id"] = seller["shop_id"]
            elem["contacts"] = seller["contacts"]
            json_service.save_to_database(db)
            return elem
    return {"message": f"Элемент с {id} не найден"}


def sellers_delete_one_by_id(id):
    db = json_service.load_from_database()
    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:
            candidate = db["sellers"].pop(i)
            json_service.save_to_database(db)
            return candidate
    return False



def sellers_create_one(seller):
    db = json_service.load_from_database()
    last_sellers_id = sellers_get_all()[-1]["id"]
    db["sellers"].append({"id": last_sellers_id + 1, **seller})
    json_service.save_to_database(db)
