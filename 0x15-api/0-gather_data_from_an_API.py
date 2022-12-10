#!/usr/bin/python3
"""fetchs user data based on the user id given as a command line argument"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    response = requests.get(url=url)

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = list(
        filter(lambda x: x.get("userId") == int(argv[1]), todos.json())
    )
    completed = list(filter(lambda x: x.get("completed"), user_todos))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            response.json().get("name"),
            len(completed),
            len(user_todos)
        )
    )
    for todo in completed:
        print("\t {}".format(todo.get('title')))
