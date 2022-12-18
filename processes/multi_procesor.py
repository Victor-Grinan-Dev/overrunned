import time
import concurrent.futures

tutorials = ["https://www.youtube.com/watch?v=fKl2JW_qrso", "https://www.youtube.com/watch?v=FsAPt_9Bf3U"]  # multiproce


# ssing, decorators


class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f"call method executed before {self.function.__name__}")
        return self.function(*args, **kwargs)


def sleeping(n=0):  # dummy function
    print(f"Sleeping for {n} seconds...")
    time.sleep(n)
    return "Done sleeping"


def execution_timer(function):
    starting_time = time.perf_counter()

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    end_time = time.perf_counter()
    print(f"performance time {round(end_time - starting_time)} second(s)")
    return wrapper


@execution_timer
def say_hi():
    print("Hi")


@Decorator
def say_bye():
    print("Bye!")


def execute_multi_processor(func, args: list = None, execution: str = "process"):
    if execution == "thread":
        with concurrent.futures.ThreadPoolExecutor() as exe:
            exe.map(func, args)
    elif execution == "thread":
        with concurrent.futures.ProcessPoolExecutor() as exe:
            exe.map(func, args)
    else:
        raise Exception  # TODO: handle exeption


say_bye()

# start = time.perf_counter()
#
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f = [executor.sudmit(sleeping, 1) for _ in range(10)]
#
#     for f in concurrent.futures.as_completed(f):
#         print(f.result())
#
# end = time.perf_counter()
#
# print(f"performance time {round(end - start), 2} second(s)")
