import time, tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

with open('input.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])
tree = [None] * (n + 1)
for i in range(1, n + 1):
    k, l, r = map(int, lines[i].split())
    tree[i] = (k, l, r)

height = [0] * (n + 1)
balance = [0] * (n + 1)

def dfs(v):
    if v == 0:
        return 0
    _, l, r = tree[v]
    hl = dfs(l)
    hr = dfs(r)
    height[v] = 1 + max(hl, hr)
    balance[v] = hr - hl
    return height[v]

if n > 0:
    dfs(1)

with open('output.txt', 'w') as f:
    for i in range(1, n + 1):
        f.write(f"{balance[i]}\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")
