import time, tracemalloc

def dfs(node, graph, visited, stack):
    visited[node] = "GRAY"
    for neighbor in graph[node]:
        if visited[neighbor] == "GRAY":
            return True
        if visited[neighbor] == "WHITE":
            if dfs(neighbor, graph, visited, stack):
                return True
    visited[node] = "BLACK"
    return False

def has_cycle(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)

    visited = {i: "WHITE" for i in range(1, n + 1)}

    for node in range(1, n + 1):
        if visited[node] == "WHITE":
            if dfs(node, graph, visited, []):
                return 1
    return 0

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]

start_time = time.perf_counter()
tracemalloc.start()

result = has_cycle(n, edges)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")