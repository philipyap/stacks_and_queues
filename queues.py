
# collections is a Python module that I am using
# deque is an object (class) on that module

from collections import deque

rome_queue = deque()
rome_queue.append(1)
rome_queue.append(5)
rome_queue.append(10)

print(rome_queue)

rome_queuepop()

print(rome_queue)

rome_list = ['work2', 'work100']

rome_list.pop(0)
print(rome_list)

# O(1)
rome = {
    "name": "Rome",
    "age": 32
}