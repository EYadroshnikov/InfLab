from flask import Flask, render_template, request, redirect, url_for
import json

import json_service
import sellers
import shops

app = Flask(__name__)
# dbbrowser
# orm
# sqlite


database_path = "database.json"

try:
    with open(database_path, "r") as f:
        pass
except FileNotFoundError:
    with open(database_path, "w") as f:
        json.dump({"autoparts": []}, f)


@app.route("/")
def index():
    autoparts = json_service.load_from_database()["autoparts"]
    return render_template("index.html", autoparts=autoparts)


@app.route("/add", methods=["POST"])
def add_autopart():
    data = json_service.load_from_database()
    autoparts = data["autoparts"]

    autopart = {
        "id": len(autoparts) + 1,
        "name": request.form["name"],
        "brand": request.form["brand"],
        "price": float(request.form["price"]),
    }

    autoparts.append(autopart)
    data["autoparts"] = autoparts
    json_service.save_to_database(data)

    return redirect(url_for("index"))


@app.route("/edit/<int:autopart_id>")
def edit_autopart(autopart_id):
    data = json_service.load_from_database()
    autoparts = data["autoparts"]

    autopart = next((item for item in autoparts if item["id"] == autopart_id), None)

    return render_template("edit.html", autopart=autopart)


@app.route("/update/<int:autopart_id>", methods=["POST"])
def update_autopart(autopart_id):
    data = json_service.load_from_database()
    autoparts = data["autoparts"]

    autopart = next((item for item in autoparts if item["id"] == autopart_id), None)

    if autopart:
        autopart["name"] = request.form["name"]
        autopart["brand"] = request.form["brand"]
        autopart["price"] = float(request.form["price"])

        json_service.save_to_database(data)

    return redirect(url_for("index"))


@app.route("/delete/<int:autopart_id>")
def delete_autopart(autopart_id):
    data = json_service.load_from_database()
    autoparts = data["autoparts"]

    autoparts = [item for item in autoparts if item["id"] != autopart_id]

    data["autoparts"] = autoparts
    json_service.save_to_database(data)

    return redirect(url_for("index"))


def get_all_by_brand(brand):
    data = json_service.load_from_database()
    autopart = list()
    for elem in data['autoparts']:
        if elem['brand'] == brand:
            autopart.append(elem)
    return autopart if autopart != [] else f"товаров бренда {brand} не найдено"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
