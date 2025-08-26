# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
            return
        print("Top\n---")
        while current:
            print(current.value)
            current = current.next
        print("---\nBottom")

    def clear(self):
        self.top = None

def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack.clear()
            print("Action performed:", action)

        elif choice == "2":
            undone_action = undo_stack.pop()
            if undone_action:
                redo_stack.push(undone_action)
                print("Undid action:", undone_action)
            else:
                print("There is no action to undo.")

        elif choice == "3":
            redone_action = redo_stack.pop()
            if redone_action:
                undo_stack.push(redone_action)
                print("Redid action:", redone_action)
            else:
                print("There is no action to redo.")

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
