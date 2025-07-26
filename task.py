import requests
import json
import csv
import os
from datetime import datetime

# 1. 


def get_single_user():
    url = "https://randomuser.me/api/"
    res = requests.get(url).json()
    user = res["results"][0]

    data = {
        "first_name": user["name"]["first"],
        "last_name": user["name"]["last"],
        "gender": user["gender"],
        "email": user["email"],
        "phone": user["phone"],
        "address": {
            "street": user["location"]["street"]["name"],
            "city": user["location"]["city"],
            "country": user["location"]["country"]
        }
    }

    with open("user.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# 2. 


def get_users_list():
    url = "https://randomuser.me/api/?results=10"
    res = requests.get(url).json()
    users = res["results"]

    data = []
    for user in users:
        data.append({
            "full_name": user["name"]["first"] + " " + user["name"]["last"],
            "email": user["email"],
            "gender": user["gender"],
            "country": user["location"]["country"]
        })

    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# 3.


def get_females():
    url = "https://randomuser.me/api/?results=10&gender=female"
    res = requests.get(url).json()
    users = res["results"]

    data = []
    for user in users:
        data.append({
            "name": user["name"]["first"] + " " + user["name"]["last"],
            "email": user["email"],
            "phone": user["phone"],
            "country": user["location"]["country"]
        })

    with open("females.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# 4.


def get_users_with_images():
    url = "https://randomuser.me/api/?results=10"
    res = requests.get(url).json()
    users = res["results"]

    data = []
    for user in users:
        data.append({
            "name": user["name"]["first"] + " " + user["name"]["last"],
            "email": user["email"],
            "image_url": user["picture"]["large"]
        })

    with open("users_with_images.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# 5. 

def get_young_users():
    url = "https://randomuser.me/api/?results=20"
    res = requests.get(url).json()
    users = res["results"]

    data = []
    for user in users:
        birth_year = int(user["dob"]["date"][:4])
        if birth_year > 1990:
            data.append({
                "name": user["name"]["first"] + " " + user["name"]["last"],
                "birth_year": birth_year,
                "email": user["email"]
            })

    with open("young_users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# 6.


def get_users_csv():
    url = "https://randomuser.me/api/?results=10"
    res = requests.get(url).json()
    users = res["results"]

    with open("users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Full Name", "Gender", "Email", "Phone", "Country"])
        for user in users:
            writer.writerow([
                user["name"]["first"] + " " + user["name"]["last"],
                user["gender"],
                user["email"],
                user["phone"],
                user["location"]["country"]
            ])


# 7.


def download_images():
    url = "https://randomuser.me/api/?results=5"
    res = requests.get(url).json()
    users = res["results"]

    if not os.path.exists("images"):
        os.mkdir("images")

    for i, user in enumerate(users, start=1):
        img_url = user["picture"]["large"]
        img_data = requests.get(img_url).content
        with open(f"images/user{i}.jpg", "wb") as f:
            f.write(img_data)


if __name__ == "__main__":
    get_single_user()
    get_users_list()
    get_females()
    get_users_with_images()
    get_young_users()
    get_users_csv()
    download_images()
    print("Barcha vazifalar bajarildi!")
