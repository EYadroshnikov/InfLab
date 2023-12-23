import json_service as json_service


# Полный список
def shop_get_all():
    db = json_service.load_from_database()
    return db["shops"]


def shop_get_one_by_name(name):
    db = json_service.load_from_database()
    for elem in db["shops"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


def shop_create_one(shop):
    db = json_service.load_from_database()
    last_sellers_id = shop_get_all()[-1]["id"]
    db["shops"].append({"id": last_sellers_id + 1, **shop})
    json_service.save_to_database(db)


def shops_delete_one_by_id(id):
    db = json_service.load_from_database()
    for i, elem in enumerate(db["shops"]):
        if elem["id"] == id:
            candidate = db["shops"].pop(i)
            for j, item in enumerate(db['sellers']):
                if item["shop_id"] == id:
                    db['sellers'].pop(i)
            return candidate
    return {"message": f"Элемент с {id} не найден"}
