# update_rectangle_json.py

import random
import json

def generate_random_rectangle():
    # Replace this with your logic to generate random values for each rectangle
    return {
        "id": random.randint(1, 100),
        "width": random.randint(1, 20),
        "height": random.randint(1, 20),
        "x": random.randint(0, 10),
        "y": random.randint(0, 10)
    }

def update_rectangle_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    new_rectangle = generate_random_rectangle()
    data.append(new_rectangle)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    file_path = "rectangle.json"
    update_rectangle_json(file_path)
