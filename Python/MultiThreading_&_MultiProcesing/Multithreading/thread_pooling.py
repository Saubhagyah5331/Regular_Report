from concurrent.futures import ThreadPoolExecutor

def task(name, age):
    print(f"Task {name} {age} is running")


with ThreadPoolExecutor(max_workers = 3) as exct:
    for i in range(5):
        exct.submit(task, i, 0)

