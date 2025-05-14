import time, tracemalloc

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M and garden[x][y] == '#'

def dfs(x, y):
    stack = [(x, y)]
    garden[x][y] = '.'
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny):
                garden[nx][ny] = '.'
                stack.append((nx, ny))

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt", "r") as f:
    N, M = map(int, f.readline().split())
    garden = [list(f.readline().strip()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if garden[i][j] == '#':
            dfs(i, j)
            count += 1

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as f:
    f.write(str(count) + "\n")
