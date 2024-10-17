import threading
import time


def print_numbers(thread_name, delay):
    for i in range(1, 6):
        time.sleep(delay)
        print(f"{thread_name}: {i}")


thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 0.5))

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Both threads have finished execution.")
