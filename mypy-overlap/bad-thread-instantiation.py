import threading


def thread_target(n: int) -> None:
    print(n**2)


thread = threading.Thread(lambda: None)  # [bad-thread-instantiation]
thread.start()
