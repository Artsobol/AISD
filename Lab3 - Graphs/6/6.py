from collections import deque
import time, tracemalloc

def bfs_shortest_path(n, edges, start, end):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]
    u, v = map(int, f.readline().split())

start_time = time.perf_counter()
tracemalloc.start()

result = bfs_shortest_path(n, edges, u, v)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")


with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
