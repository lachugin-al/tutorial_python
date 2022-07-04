#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    # pass
    stop = False
    while stop is not True:
        if wall_is_on_the_left():
            while not wall_is_on_the_right():
                move_right()
            stop = True
        else:
            while not wall_is_on_the_left():
                move_left()
            stop = True
        if wall_is_beneath():
            while not wall_is_above():
                move_up()
            stop = True
        else:
            while not wall_is_beneath():
                move_down()
            stop = True


if __name__ == '__main__':
    run_tasks()
