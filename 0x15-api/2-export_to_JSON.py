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
import sys


def main():
    """
    Main function to get data from the API and store it in a JSON file.

    The function fetches user data and tasks from the API based on the user ID
    provided as a command-line argument. It then stores the data in a JSON file
    named after the user ID.

    Command-line Arguments:
        user_id (int): The ID of the user whose data is to be fetched.

    Raises:
        IndexError: If the provided user ID does not exist.
        requests.RequestException: If there is an error in making API requests.
    """
    url = "https://jsonplaceholder.typicode.com/"

    # User Info
    user_id = sys.argv[1]
    user_url = f"{url}users?id={user_id}"
    user_data = requests.get(user_url).json()
    user_name = user_data[0].get("name")
    username = user_data[0].get("username")

    # User Tasks
    tasks_url = f"{url}todos?userId={user_id}"
    total_tasks = requests.get(tasks_url).json()
    done_tasks = requests.get(f"{tasks_url}&completed=true").json()
    total_task_num = len(total_tasks)
    done_tasks_num = len(done_tasks)

    # Store in JSON file format
    with open(f'{user_id}.json', 'w') as file:
        data = {
            user_id: [{
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            } for task in total_tasks]
        }
        json.dump(data, file)


if __name__ == "__main__":
    main()
