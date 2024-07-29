#!/usr/bin/python3
"""
This module fetching user data and tasks from an API
and storing it in a JSON file.

It includes functionalities for:
- Fetching user information
- Fetching user tasks
- Storing data in JSON format

Usage:
    python my_script.py <user_id>
"""
import json
import requests


def main():
    """
    Main function to get data from the API and store it in a JSON file.
    """
    user_id = 1
    data_dict = {}

    while True:
        url = "https://jsonplaceholder.typicode.com/"
        users = f"users?id={user_id}"
        tasks_url = f"todos?userId={user_id}"
        user_data = requests.get(f"{url}{users}").json()

        if not user_data:
            break

        username = user_data[0].get("username")
        tasks_data = requests.get(f"{url}{tasks_url}").json()

        data_dict[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks_data
        ]

        user_id += 1

    with open("todo_all_employees.json", "w") as file:
        json.dump(data_dict, file)


if __name__ == "__main__":
    main()
