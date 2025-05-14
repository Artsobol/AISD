import time
import tracemalloc
from collections import deque

tracemalloc.start()
start_time = time.perf_counter()

with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    g = [f.readline().strip() for _ in range(n)]
    qx, qy, L = map(int, f.readline().split())
    starts = [tuple(map(int, f.readline().split())) for _ in range(4)]

dist = [[-1] * m for _ in range(n)]
dq = deque()
dq.append((qx-1, qy-1))
dist[qx-1][qy-1] = 0

while dq:
    x, y = dq.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '0' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dq.append((nx, ny))

res = 0
for x, y, p in starts:
    d = dist[x-1][y-1]
    if d != -1 and d <= L:
        res += p

with open('output.txt', 'w') as f:
    f.write(str(res))

end_time = time.perf_counter()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_mem / (1024 * 1024)):.6f} Мб")
