import time, tracemalloc

def max_lectures(intervals):
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end_time = 0

    for start, end in intervals:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count


with open("input.txt", "r") as file:
    N = int(file.readline().strip())
    intervals = [tuple(map(int, file.readline().strip().split())) for _ in range(N)]


start_time = time.perf_counter()
tracemalloc.start()

result = max_lectures(intervals)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
