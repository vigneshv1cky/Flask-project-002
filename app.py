from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {"name": "Chair", "price": 15.99},
            {"name": "Table", "price": 45.50},
            {"name": "Lamp", "price": 12.75},
        ],
    },
    {
        "name": "Tech Haven",
        "items": [
            {"name": "Laptop", "price": 999.99},
            {"name": "Smartphone", "price": 699.99},
            {"name": "Headphones", "price": 149.99},
        ],
    },
    {
        "name": "Fashion Boutique",
        "items": [
            {"name": "Dress", "price": 59.99},
            {"name": "Shoes", "price": 89.99},
            {"name": "Handbag", "price": 120.00},
        ],
    },
    {
        "name": "Book Nook",
        "items": [
            {"name": "Novel", "price": 14.99},
            {"name": "Textbook", "price": 99.99},
            {"name": "Magazine", "price": 5.99},
        ],
    },
    {
        "name": "Grocery Mart",
        "items": [
            {"name": "Apples", "price": 0.99},
            {"name": "Bread", "price": 2.50},
            {"name": "Milk", "price": 3.99},
        ],
    },
]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": [request_data["items"]],
    }
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store}
    return {"message": "Store not found"}, 404


"""

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return store["items"]
    return {"message": "Store not found"}, 404
    
    """


@app.get("/store/<string:name>/item/<string:item_name>")
def get_item_in_store(name, item_name):
    for store in stores:
        if store["name"] == name:
            for item in store["items"]:
                if item["name"] == item_name:
                    return {"item": item}
            return {"message": "Item not found in the store"}, 404
    return {"message": "Store not found"}, 404
