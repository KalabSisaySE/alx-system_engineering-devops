#!/usr/bin/python3
"""fetchs all users data and exports it to json"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(url=user_url)

    all_users = {}
    for user in users.json():
        user_name = user.get("username")
        id = user.get("id")

        todos = requests.get(url=todo_url).json()
        user_todos = list(filter(lambda x: x.get("userId") == id, todos))

        todo_list = []
        for todo in user_todos:
            x = {}
            x["username"] = user_name
            x["task"] = todo.get("title")
            x["completed"] = todo.get("completed")
            todo_list.append(x)

        all_users.update({str(id): todo_list})

    with open("todo_all_employees.json", mode="w") as file:
        file.write(json.dumps(all_users))
