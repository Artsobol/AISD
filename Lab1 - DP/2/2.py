import time, tracemalloc

def min_refills(d, m, stops):
    stops = [0] + stops + [d]
    num_refills = 0
    current_pos = 0

    while current_pos < len(stops) - 1:
        last_pos = current_pos
        while (current_pos + 1 < len(stops)) and (stops[current_pos + 1] - stops[last_pos] <= m):
            current_pos += 1

        if current_pos == last_pos:
            return -1

        if current_pos < len(stops) - 1:
            num_refills += 1

    return num_refills

with open("input.txt", "r") as file:
    d = int(file.readline().strip())
    m = int(file.readline().strip())
    n = int(file.readline().strip())
    stops = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()
tracemalloc.start()

result = min_refills(d, m, stops)

current_memory, peak_memory = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
