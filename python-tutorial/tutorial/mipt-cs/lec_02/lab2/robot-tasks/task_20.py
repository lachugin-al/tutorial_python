#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    # pass
    cell_a(6)
    move_right()

def cell_a(n):
    for i in range(n):
        for i in range(1, 28, 1):
            move_right()
            fill_cell()
        move_down()
        for z in range(28, 1, -1):
            fill_cell()
            move_left()
        move_down()

if __name__ == '__main__':
    run_tasks()
