from concurrent.futures import ProcessPoolExecutor


def func():
    return "Hello world"
    

with ProcessPoolExecutor(max_workers=3) as exec:

    fut = [exec.submit(func) for _ in range(4)]
    results = [future.result() for future in fut]

    print(results)


