from sys import exit

from utils import print_menu, print_error_menu, print_main_menu
from handlers import (
    handle_add_task,
    handle_show_tasks,
    handle_show_task_detail,
    handle_mark_as_comleted,
    handle_mark_as_incomleted,
    handle_delete_task,
    handle_search_task,
    handle_register,
    handle_login,
)


def main() -> None:
    current_user = None
    while True:
        print_main_menu()

        option = input("> ")
        if option == "1":
            handle_register()
        elif option == "2":
            current_user = handle_login()
        elif option == "0":
            exit()
        else:
            print("menu xato")

        while current_user is not None:
            print_menu()

            option = input("> ")
            if option == "1":
                handle_add_task(current_user)
            elif option == "2":
                handle_show_tasks(current_user)
            elif option == "3":
                handle_show_task_detail(current_user)
            elif option == "4":
                handle_mark_as_comleted(current_user)
            elif option == "5":
                handle_mark_as_incomleted(current_user)
            elif option == "6":
                handle_delete_task(current_user)
            elif option == "7":
                handle_search_task(current_user)
            elif option == "8":
                current_user = None
            elif option == "0":
                exit()
            else:
                print_error_menu()


main()
