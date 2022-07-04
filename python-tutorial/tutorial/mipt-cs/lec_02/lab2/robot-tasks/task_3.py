#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    wall = False
    # for i in range(9):
    #     if wall_is_on_the_right():
    #        break
    #     else:
    #         move_right(1)
    # # pass

    while wall is False:
        move_right()
        if wall_is_on_the_right() is True:
            wall = True

if __name__ == '__main__':
    run_tasks()
