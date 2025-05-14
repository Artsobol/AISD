import time, tracemalloc

def balance_brackets(s):
    stack = []
    index_to_remove = set()
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(s):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if stack and stack[-1][0] == pairs[char]:
                stack.pop()
            else:
                index_to_remove.add(i)

    index_to_remove.update(i for _, i in stack)

    result = ''.join(s[i] for i in range(len(s)) if i not in index_to_remove)

    return result


with open("input.txt", "r") as file:
    s = file.readline().strip()


start_time = time.perf_counter()
tracemalloc.start()

result = balance_brackets(s)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")


with open("output.txt", "w") as file:
    file.write(result + "\n")
