import time, tracemalloc
moves = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}
with open('input.txt') as f:
    N = int(f.read())
start_time = time.perf_counter()
tracemalloc.start()
dp = [ [0]*10 for _ in range(N+1) ]
for i in range(10):
    if i != 0 and i != 8:
        dp[1][i] = 1
for l in range(2, N+1):
    for d in range(10):
        for prev in moves[d]:
            dp[l][d] = (dp[l][d] + dp[l-1][prev]) % 10**9

result = sum(dp[N]) % 10**9
end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open('output.txt', 'w') as f:
    f.write(str(result) + '\n')
