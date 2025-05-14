import time, tracemalloc

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(pattern, text):
    n, m = len(text), len(pattern)
    pi = compute_prefix_function(pattern)
    occurrences = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 2)
            j = pi[j - 1]
    return occurrences

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt", "r") as file:
    pattern = file.readline().strip()
    text = file.readline().strip()

occurrences = kmp_search(pattern, text)

with open("output.txt", "w") as file:
    file.write(f"{len(occurrences)}\n")
    file.write(" ".join(map(str, occurrences)) + "\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использование памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")
