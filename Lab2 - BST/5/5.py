import time, tracemalloc

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._exists(node.left, key)
        return self._exists(node.right, key)

    def next(self, key):
        node = self.root
        successor = None
        while node:
            if node.key > key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.key if successor else "none"

    def prev(self, key):
        node = self.root
        predecessor = None
        while node:
            if node.key < key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.key if predecessor else "none"

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

with open("input.txt", "r") as file:
    commands = file.readlines()


start_time = time.perf_counter()
tracemalloc.start()

bst = BST()
results = []

for command in commands:
    operation, x = command.split()
    x = int(x)
    if operation == "insert":
        bst.insert(x)
    elif operation == "delete":
        bst.delete(x)
    elif operation == "exists":
        results.append("true" if bst.exists(x) else "false")
    elif operation == "next":
        results.append(str(bst.next(x)))
    elif operation == "prev":
        results.append(str(bst.prev(x)))

end_time = time.perf_counter()

current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")

with open("output.txt", "w") as file:
    file.write("\n".join(results) + "\n")