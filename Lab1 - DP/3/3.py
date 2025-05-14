import time
import tracemalloc

def find_max(a, b):
    a.sort()
    b.sort()

    return sum(a[i] * b[i] for i in range(len(a)))

with open("input.txt", "r") as file:
    n = int(file.readline().strip())
    a = list(map(int, file.readline().strip().split()))
    b = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()
tracemalloc.start()

result = find_max(a, b)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")

