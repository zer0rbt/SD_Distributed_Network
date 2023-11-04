import pymongo
import os


# todo: переименовать коллекцию и название базы данных
def save_image_to_db(image_bytes: bytes, image_name: str) -> None:
    image_directory = os.path.abspath("")

    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    image_path = os.path.join(image_directory, image_name)

    client = pymongo.MongoClient("mongodb://localhost:27017/mydatabase")
    db = client["mydatabase"]
    collection = db["1"]

    image_data = {
        "name": image_name,
        "path": image_path,
        "data": image_bytes
    }
    collection.insert_one(image_data)


def get_image_from_db(image_name: str) -> bytes:
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["1"]

        image_data = collection.find_one({"name": image_name})

        if image_data:
            image_bytes = image_data.get("data", b"")
            return image_bytes
        else:
            raise ValueError(f"Изображение '{image_name}' не найдено в базе данных.")

    except Exception as e:
        raise ValueError(f"Ошибка при получении изображения из базы данных: {e}")
