import time, tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

with open('input.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])
s = [int(x) for x in lines[1:]]

INF = 10**9
dp = [[INF] * (n + 5) for _ in range(n + 1)]
used = [[False] * (n + 5) for _ in range(n + 1)]
prev = [[-1] * (n + 5) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for c in range(n + 1):
        if dp[i][c] == INF:
            continue

        new_c = c + 1 if s[i] > 100 else c
        cost = dp[i][c] + s[i]
        if cost < dp[i + 1][new_c]:
            dp[i + 1][new_c] = cost
            used[i + 1][new_c] = False
            prev[i + 1][new_c] = c

        if c >= 1:
            if dp[i][c] < dp[i + 1][c - 1]:
                dp[i + 1][c - 1] = dp[i][c]
                used[i + 1][c - 1] = True
                prev[i + 1][c - 1] = c

min_cost = INF
final_c = -1
for c in range(n + 1):
    if dp[n][c] < min_cost or (dp[n][c] == min_cost and c > final_c):
        min_cost = dp[n][c]
        final_c = c

coupons_used = []
i, c = n, final_c
while i > 0:
    pc = prev[i][c]
    if used[i][c]:
        coupons_used.append(i)
    i -= 1
    c = pc

coupons_used.sort()

with open('output.txt', 'w') as f:
    f.write(f"{min_cost}\n")
    f.write(f"{final_c} {len(coupons_used)}\n")
    for day in coupons_used:
        f.write(f"{day}\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")
