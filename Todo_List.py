import json
import math

class Todo:
    def __init__(self):
        self.tasks = self.load_todo_file()
        # find the max id or start from 1 if no tasks
        if self.tasks:
            self.next_id = max(task["id"] for task in self.tasks) + 1
        else:
            self.next_id = 1

    ### Load/make json file
    def load_todo_file(self, path = "Todo_File.json"):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def save_todo_file(self,path = "Todo_File.json"):
        with open(path, "w") as f:
            json.dump(self.tasks, f, indent=2)
        

    ### Main loop    
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

    ### add new tasks with id
    def add_task(self):
        while True:
            add_new_task = input("What would you like to add?: ").strip()
            if add_new_task:
                new_task = {"id": self.next_id, "text": add_new_task}
                self.tasks.append(new_task)
                self.next_id += 1
                self.save_todo_file()
                print("Task added!")
            another = input("Add another Task (y/n)?: ").strip().lower()
            if another == "n":
                break
            elif another == "y":
                continue
            else:
                print("Please type 'y' or 'n'.")

    ### show list of tasks with id's
    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("Task list:")
        for task in self.tasks:
            print(f"{task['id']}: {task['text']}")
                



if __name__ == "__main__":
    app = Todo()
    app.run()
