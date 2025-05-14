import time, tracemalloc

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst_height(node):
    if node is None:
        return 0
    left_height = bst_height(node.left)
    right_height = bst_height(node.right)
    return max(left_height, right_height) + 1

with open("input.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())
if N == 0:
    with open("output.txt", "w") as file:
        file.write("0\n")
    exit()


start_time = time.perf_counter()
tracemalloc.start()

nodes = {i: BSTNode(int(lines[i].split()[0])) for i in range(1, N + 1)}

for i in range(1, N + 1):
    _, left, right = map(int, lines[i].split())
    if left:
        nodes[i].left = nodes[left]
    if right:
        nodes[i].right = nodes[right]

height = bst_height(nodes[1])

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write(f"{height}\n")