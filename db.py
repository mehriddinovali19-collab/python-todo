import json


def read_file() -> list[dict]:
    f = open("db.json")
    content = f.read()
    data = json.loads(content)
    return data


def write_file(tasks: list[dict]):
    f = open("db.json", "w")
    content = json.dumps(tasks, indent=4)
    f.write(content)


def add_task(title: str, description: str, user_id: int):
    data = read_file()
    data["tasks"].append(
        {
            "id": data["current_id"],
            "title": title,
            "description": description,
            "status": False,
            "user_id": user_id,
        }
    )
    data["current_id"] += 1
    write_file(data)


def mark_task_as_completed(id: int, user_id: int):
    data = read_file()
    for task in data["tasks"]:
        if task["user_id"] == user_id and task["id"] == id:
            task["status"] = True
            write_file(data)
            return True
    return False


def mark_task_as_incompleted(id: int, user_id: int):
    data = read_file()
    for task in data["tasks"]:
        if task["user_id"] == user_id and task["id"] == id:
            task["status"] = False
            write_file(data)
            return True
    return False


def delete_task(id: int, user_id: int):
    data = read_file()
    for task in data["tasks"]:
        if task["user_id"] == user_id and task["id"] == id:
            data["tasks"].remove(task)
            write_file(data)
            return True
    return False


def get_all_tasks():
    data = read_file()
    return data["tasks"]


def get_user_by_username(username):
    data = read_file()

    for user in data["users"]:
        if user["username"] == username:
            return user
    else:
        return False


def add_user(username, password):
    data = read_file()

    new_user = {
        "id": data["current_user_id"],
        "username": username,
        "password": password,
    }
    data["users"].append(new_user)
    data["current_user_id"] += 1

    write_file(data)
