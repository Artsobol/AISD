import time, tracemalloc

def dfs(graph, node, visited):
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(graph[v])


def count_connected_components(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    for node in range(1, n + 1):
        if node not in visited:
            components += 1
            dfs(graph, node, visited)

    return components


with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]

start_time = time.perf_counter()
tracemalloc.start()

result = count_connected_components(n, edges)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")


with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
