import time, tracemalloc

def dfs1(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(neighbor, graph, visited, stack)
    stack.append(node)

def dfs2(node, transposed_graph, visited):
    visited[node] = True
    for neighbor in transposed_graph[node]:
        if not visited[neighbor]:
            dfs2(neighbor, transposed_graph, visited)

def kosaraju_scc(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    transposed_graph = {i: [] for i in range(1, n + 1)}
    visited = {i: False for i in range(1, n + 1)}
    stack = []

    for u, v in edges:
        graph[u].append(v)
        transposed_graph[v].append(u)

    for node in range(1, n + 1):
        if not visited[node]:
            dfs1(node, graph, visited, stack)

    visited = {i: False for i in range(1, n + 1)}
    scc_count = 0

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node, transposed_graph, visited)
            scc_count += 1

    return scc_count

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(m)]


start_time = time.perf_counter()
tracemalloc.start()

result = kosaraju_scc(n, edges)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
