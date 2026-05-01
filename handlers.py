from getpass import getpass

from db import (
    add_task,
    get_all_tasks,
    mark_task_as_completed,
    mark_task_as_incompleted,
    delete_task,
    get_user_by_username,
    add_user,
)


def handle_add_task(current_user):
    print("--Add New Task--")
    title = input("Title: ")
    description = input("Description: ")

    add_task(title, description, current_user["id"])

    print("Task has been added successfully.")


def handle_show_tasks(current_user):
    tasks = get_all_tasks()
    for task in tasks:
        if task["user_id"] == current_user["id"]:
            if task["status"] == False:
                print(task["id"], task["title"], "bajarilmagan")
            else:
                print(task["id"], task["title"], "bajarilgan")


def handle_show_task_detail(current_user):
    id = int(input("task id: "))
    tasks = get_all_tasks()
    for task in tasks:
        if task["user_id"] == current_user["id"]:
            if task["id"] == id:
                if task["status"] == False:
                    print(
                        task["id"], task["title"], task["description"], "bajarilmagan"
                    )
                else:
                    print(task["id"], task["title"], task["description"], "bajarilgan")


def handle_mark_as_comleted(current_user):
    id = int(input("Task id: "))
    if mark_task_as_completed(id, current_user["id"]):
        print("task bajarildi")
    else:
        print("task topilmadi")


def handle_mark_as_incomleted(current_user):
    id = int(input("Task id: "))
    if mark_task_as_incompleted(id, current_user["id"]):
        print("task bajarilmadi")
    else:
        print("task topilmadi")


def handle_delete_task(current_user):
    id = int(input("Task id: "))
    if delete_task(id, current_user["id"]):
        print("task ochirildi")
    else:
        print("task topilmadi")


def handle_search_task(current_user):
    search = input("Search: ")
    tasks = get_all_tasks()
    for task in tasks:
        if (
            task["user_id"] == current_user["id"]
            and search.lower() in task["title"]
            or search.lower() in task["description"]
        ):
            print(task["id"], task["title"], task["description"], "bajarilmagan")


def handle_register():
    username = input("username: ")
    password = getpass("password: ")
    confirm = getpass("confirm: ")

    existing_user = get_user_by_username(username)
    if existing_user != False:
        print("username already exists.")
        return

    if password != confirm:
        print("password va confirm teng emas.")
        return

    add_user(username, password)
    print("siz muvaffaqiyatli royxatdan otdingiz.")


def handle_login():
    username = input("username: ")
    password = getpass("password: ")

    existing_user = get_user_by_username(username)
    if existing_user == False:
        print("username topilmadi.")
        return

    if existing_user["password"] != password:
        print("password xato")
        return

    print("siz muvaffaqiyatli login boldingiz.")

    return existing_user
