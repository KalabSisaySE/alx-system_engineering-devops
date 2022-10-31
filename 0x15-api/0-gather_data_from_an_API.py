#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
from sys import argv
from urllib import request
from sys import argv

if __name__ == "__main__":
    emp_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/todos/"

    with request.urlopen(emp_url) as response:
        emp_data = json.loads(response.read())

    with request.urlopen(todo_url) as res:
        todos = json.loads(res.read())
        total = [todo for todo in todos if todo.get("userId") == int(argv[1])]
        completed = [todo for todo in todos if todo.get("userId")
                     == int(argv[1]) and todo.get("completed")]

    print(
        "Employee {} is done with tasks ({}/{})".format(
            emp_data["name"], len(completed), len(total))
    )
    for task in completed:
        print("\t {}".format(task["title"]))
