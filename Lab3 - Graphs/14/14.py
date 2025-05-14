import heapq, time, tracemalloc

def dijkstra(n, d, v, bus_routes):
    graph = {i: [] for i in range(1, n + 1)}

    for u, start_time, dest, arrival_time in bus_routes:
        graph[u].append((start_time, dest, arrival_time))

    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[d] = 0

    pq = [(0, d)]

    while pq:
        cur_time, cur_village = heapq.heappop(pq)

        if cur_village == v:
            return cur_time

        for start_time, next_village, arrival_time in graph[cur_village]:
            if cur_time <= start_time and arrival_time < min_time[next_village]:
                min_time[next_village] = arrival_time
                heapq.heappush(pq, (arrival_time, next_village))

    return -1

with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    d, v = map(int, f.readline().split())
    r = int(f.readline().strip())
    bus_routes = [tuple(map(int, f.readline().split())) for _ in range(r)]


start_time = time.perf_counter()
tracemalloc.start()

result = dijkstra(n, d, v, bus_routes)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время алгоритма: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
