import json

class Todo:
    def __init__(self):
        self.tasks = []
    
    def run(self):
        while True:
            choice = input(
                "What would you like to do?\n"
                "Add new task (a):\n"
                "Edit task (e):\n" 
                "See all tasks (s):\n" 
                "Quit (q):\n> "
            ).strip().lower()

            if choice == "q":
                print("Bye!")
                break
            elif choice == "a":
                self.add_task()
            elif choice == "s":
                self.show_tasks()
            else:
                print("Please choose a, s, or q.")
class DataBase:
    def __init__(self, path = "Todo_File.json"):
        self.task_file = path

    def load_todo_file(self):
        try:
            with open(self.task_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_task(self):
        while True:
            add_new_task = input("What would you like to add?: ").strip()
            if add_new_task:
                self.tasks.append(add_new_task)
                print("Task added!")
            another = input("Add another Task (y/n)?: ").strip().lower()
            if another == "n":
                break
            elif another == "y":
                continue
            else:
                print("Please type 'y' or 'n'.")


    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("Task list:")
        for i, t in enumerate(self.tasks, start=1):
            print(f"{i}. {t}")


if __name__ == "__main__":
    app = Todo()
    app.run()
