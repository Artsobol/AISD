import time, tracemalloc

def rabin_karp(pattern, text, prime=10**9 + 7, base=31):
    m, n = len(pattern), len(text)
    pattern_hash = 0
    current_hash = 0
    base_pow = 1
    positions = []

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        current_hash = (current_hash * base + ord(text[i])) % prime
        if i > 0:
            base_pow = (base_pow * base) % prime

    if pattern_hash == current_hash and text[:m] == pattern:
        positions.append(1)

    for i in range(m, n):
        current_hash = (current_hash - ord(text[i - m]) * base_pow) % prime
        current_hash = (current_hash * base + ord(text[i])) % prime
        current_hash = (current_hash + prime) % prime
        if current_hash == pattern_hash and text[i - m + 1:i + 1] == pattern:
            positions.append(i - m + 2)

    return positions

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt", "r") as fin:
    pattern, text = fin.read().strip().split("\n")

positions = rabin_karp(pattern, text)

with open("output.txt", "w") as fout:
    fout.write(f"{len(positions)}\n")
    fout.write(" ".join(map(str, positions)) + "\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

