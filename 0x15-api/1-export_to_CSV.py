#!/usr/bin/python3
"""using this REST API & returns data about user tasks"""
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
    username = user_data[0].get("username")
    # User Tasks
    tasks_url = f"{url}todos?userId={user_id}"
    total_tasks = requests.get(f"{tasks_url}").json()
    done_tasks = requests.get(f"{tasks_url}&completed=true").json()
    total_task_num = len(total_tasks)
    done_tasks_num = len(done_tasks)

    # Store in .csv file
    with open(f'{user_id}.csv', 'w') as file:
        for task in total_tasks:
            task_status = task["completed"]
            task_title = task["title"]
            data = f'"{user_id}","{username}","{task_status}","{task_title}"'
            file.write(data + '\n')


if __name__ == "__main__":
    main()
