#!/usr/bin/python3
"""gathers user data from the RESTAPI and exports it to json"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_name = requests.get(url=user_url).json().get("username")
    response = requests.get(url=todos_url)
    user_todos = list(
        filter(lambda x: x.get("userId") == int(argv[1]), response.json())
    )

    todo_list = []
    for todo in user_todos:
        x = {}
        x["task"] = todo.get("title")
        x["completed"] = todo.get("completed")
        x["username"] = user_name
        todo_list.append(x)

    with open(str(argv[1] + ".json"), mode="w") as file:
        file.write(json.dumps({argv[1]: todo_list}))
