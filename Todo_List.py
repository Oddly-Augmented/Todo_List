import json


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
            elif choice == "e":
                self.edit_task()
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


    def edit_task(self):
        if not self.tasks:
            print("No tasks to edit.")
            return
        
        self.show_tasks()
        while True:
            id_input = input("What task by number would you like to edit: ").strip()
            if id_input == "q":
                break
            elif not id_input.isdigit():
                print("Please enter a valid number.")
                continue
            else:
                print("Please enter a valid number.")

            task_id = int(id_input)
            task = next((t for t in self.tasks if t["id"] == task_id), None)
            if task is None:
                print("No task with that id. Try again.")
                continue

            print(f"Current text: {task['text']}")
            edit_task_input = input(
                "What would you like to do?\n"
                "Edit task (e):\n" 
                "Delete task (d):\n" 
                "Quit (q):\n> "
            ).strip().lower()

            if edit_task_input == "q":
                print("Bye!")
                break
            elif edit_task_input == "e":
                new_text = input("New text (leave blank to cancel): ").strip()
                if not new_text:
                    print("Edit cancelled.")
                    return
                
                task["text"] = new_text
                self.save_todo_file()
                print("Task updated.")
                return
            elif edit_task_input == "d":
                self.tasks = [t for t in self.tasks if t["id"] != task_id]
                self.save_todo_file()
                print("Task deleted.")
                return
            else:
                print("Please choose e, d, or q.")




        

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
