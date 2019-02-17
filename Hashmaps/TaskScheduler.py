"""
Problem:
We have scheduler performs tasks. Task types are identified with an integer id.
Each task takes 1 interval to complete and once it’s complete we take a cooldown of X intervals
before another task of the same type can be run. However, we can still run other tasks with different ids.
The cooldown is the same for all task types.

Constraint: We must always run all tasks in the order we receive them (serially)

Return: An integer representing the minimum intervals needed to process all tasks
"""


# Hashmap
def task_scheduler(tasks, cooldown):
    next_start_time = {}

    intervals = 0
    for task in tasks:
        if task in next_start_time and next_start_time[task] > intervals:
            intervals = next_start_time[task]
            next_start_time[task] = intervals + (cooldown + 1)
        else:
            intervals += 1
            next_start_time[task] = intervals + (cooldown + 1)
    return intervals


tasks = [3, 4, 5, 3, 4, 5]
cool = 4
print(task_scheduler(tasks, cool) == 8)

tasks = [1,1,2,1]
cool = 2
print(task_scheduler(tasks, cool) == 7)

tasks = [1,2,3,1,2,3]
cool = 3
print(task_scheduler(tasks, cool) == 7)

tasks = [1,2,3,4,5,6,2,4,6,1,2,4]
cool = 6
print(task_scheduler(tasks, cool) == 18)