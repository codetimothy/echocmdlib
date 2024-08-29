from echocmdlib import clear_screen, print_menu, get_user_choice
from echocmdlib.colors import rainbow_text
from echocmdlib.progress import show_progress
from echocmdlib.loglib import *
from echocmdlib.ui import *
from echocmdlib.title import *
import time


def main():
    while True:
        clear_screen()
        print_title("THIS IS A TEST")
        menu_options = ["执行事例日志", "调出输入框", "执行进度条", "调出等待", "退出"]
        print_menu(menu_options)

        choice = get_user_choice(len(menu_options))

        if choice == 1:
            print(rainbow_text("执行事例日志"))
            time.sleep(0.7)
            clear_screen()
            print_log_IWE("This is the test", "info")
            time.sleep(0.5)
            print_log_IWE("This is the test", "warn")
            time.sleep(0.5)
            print_log_IWE("This is the test", "error")
            time.sleep(0.5)

        elif choice == 2:
            print(rainbow_text("调出输入框"))
            result = input_get("要不随便输入些什么：")
            print("你输入了: " + rainbow_text(result))

        elif choice == 3:
            print(rainbow_text("执行进度条"))
            show_progress("执行任务", total=100)
        elif choice == 4:
            waiting("等待...", "dots", "time.sleep(5)")
        elif choice == 5:
            print(rainbow_text("再见!"))
            time.sleep(0.5)
            clear_screen()
            break

        input(rainbow_text("\n按Enter键继续..."))


if __name__ == "__main__":
    main()
