import time, tracemalloc

def build_hashes(s):
    n = len(s)
    m1, m2 = 10**9+7, 10**9+9
    x = 91138233
    h1, h2 = [0]*(n+1), [0]*(n+1)
    p1, p2 = [1]*(n+1), [1]*(n+1)
    for i in range(1, n+1):
        c = ord(s[i-1]) - ord('a') + 1
        h1[i] = (h1[i-1]*x + c) % m1
        h2[i] = (h2[i-1]*x + c) % m2
        p1[i] = (p1[i-1]*x) % m1
        p2[i] = (p2[i-1]*x) % m2
    return h1, h2, p1, p2, m1, m2

def eq_sub(i, j, L, h1, h2, p1, p2, m1, m2):
    a1 = (h1[i+L] - h1[i]*p1[L] % m1 + m1) % m1
    b1 = (h1[j+L] - h1[j]*p1[L] % m1 + m1) % m1
    if a1 != b1: return False
    a2 = (h2[i+L] - h2[i]*p2[L] % m2 + m2) % m2
    b2 = (h2[j+L] - h2[j]*p2[L] % m2 + m2) % m2
    return a2 == b2

start_time = time.perf_counter()
tracemalloc.start()
with open('input.txt','r',encoding='utf-8') as f:
    s = f.readline().strip()
n = len(s)

h1,h2,p1,p2,m1,m2 = build_hashes(s)

INF = 10**18
dp = [INF]*(n+1)
rep = ['']*(n+1)
dp[0]=0

for i in range(n):
    for L in range(1, n-i+1):
        k = 1
        while i + L*(k+1) <= n and eq_sub(i, i+L*k, L, h1,h2,p1,p2,m1,m2):
            k += 1
        for t in range(1, k+1):
            j = i + L*t
            cost = L
            if t > 1:
                cost += 1 + len(str(t))
            new_cost = dp[i] + (0 if dp[i]==0 else 1) + cost
            if new_cost < dp[j]:
                dp[j] = new_cost
                block = s[i:i+L]
                suffix = f"*{t}" if t>1 else ''
                rep[j] = (rep[i] + ('+' if dp[i]>0 else '') + block + suffix)

with open('output.txt','w',encoding='utf-8') as f:
    f.write(rep[n])

end_time = time.perf_counter()
cur_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Время выполнения: {(end_time-start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_mem/(1024*1024)):.6f} Мб")
