import heapq, time, tracemalloc

def dijkstra(n, edges, start, end):
    graph = {i: [] for i in range(1, n + 1)}

    for u, v, w in edges:
        graph[u].append((v, w))

    min_dist = {i: float('inf') for i in range(1, n + 1)}
    min_dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > min_dist[cur_node]:
            continue

        for neighbor, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < min_dist[neighbor]:
                min_dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return min_dist[end] if min_dist[end] != float('inf') else -1

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]
    u, v = map(int, f.readline().split())

start_time = time.perf_counter()
tracemalloc.start()

result = dijkstra(n, edges, u, v)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
