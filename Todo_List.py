class Todo:
    def __init__(self):
        pass
    # def tasks(self, id, description, status, created_at, updated_at):
    #     self.id = id
    def add_task(self,tasks):
        user_choice = input("Would you like to add a task (y/n)?: ").strip().lower()
        tasks = []
        if user_choice == "n":
            return
        elif user_choice == "y":
            tasks = input("What would you like to add?:\n ")
            print(tasks)
        else:
            print("Please chose 'y' or 'n': ")


if __name__ == "__main__":
    task = Todo()
    task.add_task()
