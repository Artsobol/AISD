import time
import tracemalloc

def count_almost_palindromes(N, K, S):
    dp = [[0] * N for _ in range(N)]
    count = 0

    for length in range(1, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if i >= j:
                dp[i][j] = 0
            else:
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 1
            if dp[i][j] <= K:
                count += 1
    return count

with open("input.txt", "r") as file:
    N, K = map(int, file.readline().strip().split())
    S = file.readline().strip()

start_time = time.perf_counter()
tracemalloc.start()

result = count_almost_palindromes(N, K, S)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
