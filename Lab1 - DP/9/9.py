import time, tracemalloc

def min_cost(N, costs):
    size = [1, 10, 100, 1000, 10000, 100000, 1000000]

    min_cost = [float('inf')] * (N + 1)
    min_cost[0] = 0

    for i in range(1, N + 1):
        for j in range(len(size)):
            if i >= size[j]:
                min_cost[i] = min(min_cost[i], min_cost[i - size[j]] + costs[j])
            else:
                min_cost[i] = min(min_cost[i], costs[j])

    return min_cost[N]

with open("input.txt", "r") as file:
    N = int(file.readline().strip())
    costs = [int(file.readline().strip()) for _ in range(7)]

start_time = time.perf_counter()
tracemalloc.start()

result = min_cost(N, costs)


end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
