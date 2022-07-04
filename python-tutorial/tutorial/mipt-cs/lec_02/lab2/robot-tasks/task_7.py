#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    # pass
    while not wall_is_beneath():
        move_down()
    for i in range(20):
        if wall_is_beneath():
            move_right()
    move_down()
    for i in range(20):
        if wall_is_on_the_left() is not True:
            move_left()

if __name__ == '__main__':
    run_tasks()
