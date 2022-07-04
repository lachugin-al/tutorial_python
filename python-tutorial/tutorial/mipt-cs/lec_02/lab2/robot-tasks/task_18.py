#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    # pass
    while not wall_is_on_the_right():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
        elif wall_is_on_the_right():
            break
        else:
            move_right()
    while not wall_is_on_the_left():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
        elif wall_is_on_the_left():
            break
        else:
            move_left()



if __name__ == '__main__':
    run_tasks()
