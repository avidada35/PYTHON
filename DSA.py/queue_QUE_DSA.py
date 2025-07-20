"""Design a food ordering system where your python program will run two threads,

1]Place Order: This thread will be placing an order and inserting that into a queue. 
  This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
2]Serve Order: This thread will server the order. 
   All you need to do is pop the order out of the queue and print it. 
   This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started."""


#orders = ['pizza','samosa','pasta','biryani','burger']

import threading
import queue
import time

class FoodOrderingSystem:
    def __init__(self):
        self.order_queue = queue.Queue()

    # Function for placing orders
    def place_order(self):
        orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
        for order in orders:
            self.order_queue.put(order)
            print(f"Order placed: {order}")
            time.sleep(5)

    # Function for serving orders
    def serve_order(self):
        time.sleep(1)  # Start serving orders 1 second after placing orders
        while True:
            if not self.order_queue.empty():
                order = self.order_queue.get()
                print(f"Serving order: {order}")
                time.sleep(10)
            else:
                print("No more orders to serve")
                break

# Create an instance of the FoodOrderingSystem class
food_ordering_system = FoodOrderingSystem()

# Create and start threads for placing and serving orders
place_order_thread = threading.Thread(target=food_ordering_system.place_order)
serve_order_thread = threading.Thread(target=food_ordering_system.serve_order)

place_order_thread.start()
serve_order_thread.start()

# Join the threads to wait for them to finish
place_order_thread.join()
serve_order_thread.join()

print("All orders served. Exiting...")
