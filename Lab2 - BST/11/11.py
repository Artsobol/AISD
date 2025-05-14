import time, tracemalloc

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _balance(self, node):
        if not node:
            return node
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return self._balance(node)

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._exists(node.left, key)
        else:
            return self._exists(node.right, key)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

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

with open("input.txt", "r") as file:
    commands = file.readlines()

start_time = time.perf_counter()
tracemalloc.start()

tree = AVLTree()
results = []

for command in commands:
    if not command.strip():
        continue
    operation, x = command.split()
    x = int(x)

    if operation == "insert":
        tree.insert(x)
    elif operation == "delete":
        tree.delete(x)
    elif operation == "exists":
        results.append("true" if tree.exists(x) else "false")
    elif operation == "next":
        results.append(str(tree.next(x)))
    elif operation == "prev":
        results.append(str(tree.prev(x)))

with open("output.txt", "w") as file:
    file.write("\n".join(results) + "\n")

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")
