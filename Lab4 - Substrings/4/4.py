import time, tracemalloc

def build_hashes(s):
    n = len(s)
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    x  = 91138233
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    p1 = [1] * (n + 1)
    p2 = [1] * (n + 1)
    for i in range(1, n + 1):
        c     = ord(s[i-1]) - ord('a') + 1
        h1[i] = (h1[i-1] * x + c) % m1
        h2[i] = (h2[i-1] * x + c) % m2
        p1[i] = (p1[i-1] * x)      % m1
        p2[i] = (p2[i-1] * x)      % m2
    return h1, h2, p1, p2, m1, m2

def substrings_equal(a, b, length, h1, h2, p1, p2, m1, m2):
    ha1 = (h1[a + length] - h1[a] * p1[length] % m1 + m1) % m1
    hb1 = (h1[b + length] - h1[b] * p1[length] % m1 + m1) % m1
    if ha1 != hb1:
        return False
    ha2 = (h2[a + length] - h2[a] * p2[length] % m2 + m2) % m2
    hb2 = (h2[b + length] - h2[b] * p2[length] % m2 + m2) % m2
    return ha2 == hb2

def check_queries(s, queries):
    h1, h2, p1, p2, m1, m2 = build_hashes(s)
    results = []
    for a, b, length in queries:
        results.append("Yes" if substrings_equal(a, b, length, h1, h2, p1, p2, m1, m2) else "No")
    return results

start_time = time.perf_counter()
tracemalloc.start()

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
s = lines[0].strip()
q = int(lines[1].strip())
queries = [tuple(map(int, line.split())) for line in lines[2:2 + q]]

answers = check_queries(s, queries)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(answers))

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")




































