#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    check_walls()
    # pass

def check_walls():
    if wall_is_on_the_right():
        if wall_is_above():
            if wall_is_on_the_left():
                if wall_is_beneath():
                    print('wall around')
                else: move_down()
            else: move_left()
        else: move_up()
    else: move_right()

if __name__ == '__main__':
    run_tasks()
