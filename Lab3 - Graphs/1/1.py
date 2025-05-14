import time, tracemalloc

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        stack.extend(graph[node])


def is_path_exists(n, edges, u, v):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    dfs(graph, u, visited)
    return 1 if v in visited else 0

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]
    u, v = map(int, f.readline().split())

start_time = time.perf_counter()
tracemalloc.start()

result = is_path_exists(n, edges, u, v)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
