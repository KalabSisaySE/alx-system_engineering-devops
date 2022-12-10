#!/usr/bin/python3
"""gathers user data from API and exports it to csv"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]

    response = requests.get(url=url)
    user_name = requests.get(url=user_url).json().get("username")

    user_todos = list(
        filter(lambda x: x.get("userId") == int(argv[1]), response.json())
    )
    with open(str(argv[1] + ".csv"), mode="w") as file:
        user_writer = csv.writer(file, delimiter=",", quotechar='"', quoting=1)
        for todo in user_todos:
            user_writer.writerow(
                [
                    todo.get("userId"),
                    user_name,
                    todo.get("completed"),
                    todo.get("title"),
                ]
            )
