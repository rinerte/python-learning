# # threading

# # thread = a flow of execution. like a separate order of instructions.
# #          however each thread takes a turn running to achieve concurrency.
# #          GIL = (global interpreter lock), a lock that allows only one thread to hold
# #          the control of the Python interpreter. (to prevent data corruption)

# # cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
# # use multiprocessing

# # io bound = program/task spends most of its time waiting for external events (user input, web scraping, database)
# # use multithreading

# import threading
# import time

# # print(threading.active_count())
# # print(threading.enumerate())

# start = time.perf_counter()

# def eat_breakfast():
#     time.sleep(3)
#     print("You finished eating breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("You finished drinking coffee")

# def study():
#     time.sleep(5)
#     print("You finished studying")

# # eat_breakfast()
# # drink_coffee()
# # study()

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
# z = threading.Thread(target=study, args=())
# z.start()
# print(threading.active_count())
# print(threading.enumerate())

# x.join()
# y.join()
# z.join()
# # performance counter in seconds

# print(f"Total time: {time.perf_counter()-start} seconds")


# daemon thread = a thread that runs in the background, not important for program to run.
#                 your program will not wait for daemon threads to complete before exiting.
#                 non-daemon threads cannot normally be killed, they run until completion.  
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count +=1
        print("logged in for: ",count," seconds")

x = threading.Thread(target=timer, daemon=True)
# x.setDaemon(True)
x.start()
print(x.daemon)

answer = input("Do you wish to exit?")