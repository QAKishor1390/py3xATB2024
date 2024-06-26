def my_decorator(func):
    def wrapper():
        print("Start......")
        print("************")
        func()
        print("************")
        print("End......")

    return wrapper()


@my_decorator
def hello():
    print("Say Hello")
