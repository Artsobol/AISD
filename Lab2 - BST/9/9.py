import time, tracemalloc
from collections import deque

start_time = time.perf_counter()
tracemalloc.start()

with open('input.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])
raw_tree = {}
key_to_index = {}

for i in range(1, n + 1):
    k, l, r = map(int, lines[i].split())
    raw_tree[i] = (k, l, r)
    key_to_index[k] = i

m = int(lines[n + 1])
delete_keys = list(map(int, lines[n + 2].split()))

def build_children(tree):
    children = {}
    for i, (_, l, r) in tree.items():
        if i not in children:
            children[i] = []
        if l != 0:
            children[i].append(l)
        if r != 0:
            children[i].append(r)
    return children

def collect_subtree_nodes(start, children):
    result = set()
    q = deque([start])
    while q:
        u = q.popleft()
        result.add(u)
        for v in children.get(u, []):
            q.append(v)
    return result

with open('output.txt', 'w') as f:
    current_tree = raw_tree.copy()
    for k in delete_keys:
        if k in key_to_index and key_to_index[k] in current_tree:
            root = key_to_index[k]
            children = build_children(current_tree)
            to_delete = collect_subtree_nodes(root, children)
            for d in to_delete:
                current_tree.pop(d, None)
        f.write(f"{len(current_tree)}\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")
