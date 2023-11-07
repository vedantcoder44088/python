import threading
import time

# Function for the first thread
def thread_one_function():
    print("Thread One is starting...")
    for i in range(5):
        print("Thread One is executing")
        time.sleep(1)
    print("Thread One is ending...")

# Function for the second thread
def thread_two_function():
    print("Thread Two is starting...")
    for i in range(5):
        print("Thread Two is executing")
        time.sleep(1)
    print("Thread Two is ending...")

# Create the first thread
thread_one = threading.Thread(target=thread_one_function)

# Create the second thread
thread_two = threading.Thread(target=thread_two_function)

# Start both threads
thread_one.start()
thread_two.start()

# Join both threads
thread_one.join()
thread_two.join()

# Main thread prints this when both threads are done
print("Both threads have finished their execution.")
