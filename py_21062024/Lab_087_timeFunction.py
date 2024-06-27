import time


def note_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken " + str(end_time - start_time))

    return wrapper()


@note_time
def logs_function():
    time.sleep(10)
    # print("print the logs of time taken")
