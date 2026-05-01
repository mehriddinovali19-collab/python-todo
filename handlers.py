from db import (
    add_task,
    get_all_tasks,
    mark_task_as_completed,
    mark_task_as_incompleted,
    delete_task,
)


def handle_add_task():
    print("--Add New Task--")
    title = input("Title: ")
    description = input("Description: ")

    add_task(title, description)

    print("Task has been added successfully.")


def handle_show_tasks():
    tasks = get_all_tasks()
    for task in tasks:
        if task["status"] == False:
            print(task["id"], task["title"], "bajarilmagan")
        else:
            print(task["id"], task["title"], "bajarilgan")


def handle_show_task_detail():
    id = int(input("task id: "))
    tasks = get_all_tasks()
    for task in tasks:
        if task["id"] == id:
            if task["status"] == False:
                print(task["id"], task["title"], task["description"], "bajarilmagan")
            else:
                print(task["id"], task["title"], task["description"], "bajarilgan")


def handle_mark_as_comleted():
    id = int(input("Task id: "))
    if mark_task_as_completed(id):
        print("task bajarildi")
    else:
        print("task topilmadi")


def handle_mark_as_incomleted():
    id = int(input("Task id: "))
    if mark_task_as_incompleted(id):
        print("task bajarilmadi")
    else:
        print("task topilmadi")


def handle_delete_task():
    id = int(input("Task id: "))
    if delete_task(id):
        print("task ochirildi")
    else:
        print("task topilmadi")


def handle_search_task():
    search = input("Search: ")
    tasks = get_all_tasks()
    for task in tasks:
        if search.lower() in task["title"] or search.lower() in task["description"]:
            print(task["id"], task["title"], task["description"], "bajarilmagan")
