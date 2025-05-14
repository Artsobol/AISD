from collections import deque
import tracemalloc, time

def bfs(reactions, start, target):
    if start == target:
        return 0

    graph = {}
    for reaction in reactions:
        src, dest = reaction.split(" -> ")
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, steps = queue.popleft()

        if current not in graph:
            continue

        for neighbor in graph[current]:
            if neighbor == target:
                return steps + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1


with open("input.txt", "r") as f:
    m = int(f.readline().strip())
    reactions = [f.readline().strip() for _ in range(m)]
    start = f.readline().strip()
    target = f.readline().strip()

start_time = time.perf_counter()
tracemalloc.start()

result = bfs(reactions, start, target)

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
