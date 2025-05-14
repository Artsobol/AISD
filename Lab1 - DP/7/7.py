import time
import tracemalloc

def max_repair(K, repair_times):
    repair_times.sort()

    boots_repaired = 0
    total_time = 0

    for current_time in repair_times:
        if total_time + current_time <= K:
            total_time += current_time
            boots_repaired += 1
        else:
            break

    return boots_repaired

with open("input.txt", "r") as file:
    K, n = map(int, file.readline().strip().split())
    repair_times = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()
tracemalloc.start()

result = max_repair(K, repair_times)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
