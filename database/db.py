import os


# todo: переименовать коллекцию и название базы данных
def save_image_to_db(image_bytes: bytes, image_name: str) -> None:
    image_directory = os.getenv("IMAGES_PATH")

    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    image_path = os.path.join(image_directory, image_name)

    file = open(image_path, "wb")
    file.write(image_bytes)
    file.close()


def get_image_from_db(image_name: str) -> bytes:
    image_path = os.path.join(os.getenv("IMAGES_PATH"), image_name)

    if not os.path.exists(image_path):
        raise ValueError(f"Изображение '{image_name}' не найдено в базе данных.")

    file = open(image_path)
    image_data = file.read()
    file.close()

    return image_data
