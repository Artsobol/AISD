import time, tracemalloc

def prefix_function(s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        j = p[i-1]
        while j > 0 and s[j] != s[i]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


with open("input.txt", "r") as file:
    s = file.readline().strip()

start_time = time.perf_counter()
tracemalloc.start()

result = prefix_function(s)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, result)) + "\n")

