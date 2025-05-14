import time, tracemalloc

class BST:
    def __init__(self):
        self.data = []

    def insert(self, x):
        if x not in self.data:
            self.data.append(x)
            self.data.sort()

    def kth_element(self, k):
        return self.data[k - 1] if 1 <= k <= len(self.data) else "0"

start_time = time.perf_counter()
tracemalloc.start()

bst = BST()
results = []

with open("input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        command, x = parts[0], int(parts[1])
        if command == '+':
            bst.insert(x)
        elif command == '?':
            results.append(str(bst.kth_element(x)))

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write("\n".join(results) + "\n")