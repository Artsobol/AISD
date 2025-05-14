import time, tracemalloc

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return

    def next(self, x):
        answer = None
        current = self.root
        while current:
            if current.key > x:
                answer = current.key
                current = current.left
            else:
                current = current.right
        return answer if answer is not None else 0

start_time = time.perf_counter()
tracemalloc.start()

bst = BST()
output_lines = []

with open("input.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        op, x_str = line.split()
        x = int(x_str)
        if op == '+':
            bst.insert(x)
        elif op == '>':
            result = bst.next(x)
            output_lines.append(str(result))


end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as outfile:
    outfile.write("\n".join(output_lines) + "\n")
