import time, tracemalloc

def fractional_knapsack(W, items):
    filtered_items = [(v, w, v / w) for v, w in items if w > 0]
    filtered_items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    for value, weight, ratio in filtered_items:
        if W == 0:
            break
        take = min(weight, W)
        total_value += take * ratio
        W -= take

    return total_value

with open("input.txt", "r") as file:
    n, W = map(int, file.readline().strip().split())
    items = [tuple(map(int, file.readline().strip().split())) for _ in range(n)]

start_time = time.perf_counter()
tracemalloc.start()

result = fractional_knapsack(W, items)

current_memory, peak_memory = tracemalloc.get_traced_memory()
end_time = time.perf_counter()


print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(f"{result:.4f}\n")
