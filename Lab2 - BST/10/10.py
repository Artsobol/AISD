import time
import tracemalloc

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.key < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.key) and
            is_valid_bst(node.right, node.key, max_val))

with open("input.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())
if N == 0:
    with open("output.txt", "w") as file:
        file.write("YES\n")
    exit()

start_time = time.perf_counter()
tracemalloc.start()

nodes = [BSTNode(int(lines[i + 1].split()[0])) for i in range(N)]

for i in range(N):
    parts = list(map(int, lines[i + 1].split()))
    key, left, right = parts[0], parts[1], parts[2]
    if left != 0:
        nodes[i].left = nodes[left - 1]
    if right != 0:
        nodes[i].right = nodes[right - 1]

is_bst = is_valid_bst(nodes[0])

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write("YES\n" if is_bst else "NO\n")
