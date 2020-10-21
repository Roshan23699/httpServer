import time
from threading import Thread
import sys
# start_time = time.time()
# sec = 4
# string = ''
# while True:
#     string += str(input())
#     current_time = time.time()
#     elapsed_time = current_time - start_time
#     if elapsed_time > sec:
#         print("finished iterating ")
#         break
def tp():
    while True:
        string = str(input())

    print(string)

new_thread = Thread(target=tp, args=[])
new_thread.start()
new_thread.join(timeout=1.0)
sys.exit()
print("hi")
