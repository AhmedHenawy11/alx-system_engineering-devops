#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID, returns information about his/her"""
import requests
import sys


def main():
    """ main function to get data from api """

    url = "https://jsonplaceholder.typicode.com/"
    # User Info
    user_id = sys.argv[1]
    user_url = f"{url}users?id={user_id}"
    user_data = requests.get(user_url).json()
    user_name = user_data[0].get("name")
    # User Tasks
    tasks_url = f"{url}todos?userId={user_id}"
    total_tasks = requests.get(f"{tasks_url}").json()
    done_tasks = requests.get(f"{tasks_url}&completed=true").json()
    total_task_num = len(total_tasks)
    done_tasks_num = len(done_tasks)

    # Print the result in format
    print(f"Employee {user_name} is done with tasks({done_tasks_num}/{total_task_num}):")
    for task in done_tasks:
        print("\t " + task.get("title"))


if __name__ == "__main__":
    main()
