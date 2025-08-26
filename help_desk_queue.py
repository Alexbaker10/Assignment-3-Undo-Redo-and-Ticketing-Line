# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None 
        return removed_node.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
	
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        print("Front\n---")
        while current:
            print(current.value)
            current = current.next 
        print("---\nBack")
    
    
def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(name, " added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print("Helped customer: ", customer)
            else:
                print("No customers are waiting.")


        elif choice == "3":
            customer = queue.peek()
            if customer:
                print("Next customer is: ", customer)
            else:
                print("No customers are waiting.")


        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
