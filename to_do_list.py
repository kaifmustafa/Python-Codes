def show_todos(todos):
    if not todos:
        print("No tasks in your to-do list!")
    else:
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

def add_todo(todos):
    todo = input("Enter a task to add to your to-do list: ")
    todos.append(todo)
    print(f"Task '{todo}' added to the list.")

def remove_todo(todos):
    show_todos(todos)
    task_num = int(input("Enter the task number to remove: "))
    if task_num <= len(todos):
        removed = todos.pop(task_num - 1)
        print(f"Task '{removed}' removed from the list.")
    else:
        print("Invalid task number!")

def to_do_list():
    todos = []
    while True:
        print("\nTo-Do List:")
        print("1. Show To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            show_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            print("Exiting To-Do List!")
            break
        else:
            print("Invalid input! Please choose between 1-4.")

# Run the to-do list
if __name__ == "__main__":
    to_do_list()
