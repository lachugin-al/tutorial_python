#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    # pass
    stop = False
    while stop is not True:
        if wall_is_on_the_right():
            stop = True
        if not (wall_is_beneath() and wall_is_above()):
            if wall_is_above():
                cell_down()
            elif wall_is_beneath():
                cell_up()
            else:
                cell_down()
                cell_up()
        if stop is not True:
            move_right()

def cell_up():
    move_up()
    fill_cell()
    move_down()

def cell_down():
    move_down()
    fill_cell()
    move_up()

if __name__ == '__main__':
    run_tasks()
