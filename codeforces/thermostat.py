def min_operations(l, r, x, a, b):
    if a == b:
        return 0
    if abs(a - b) >= x:
        return 1
    if abs(a - l) >= x and abs(b - l) >= x:
        return 2
    if abs(a - r) >= x and abs(b - r) >= x:
        return 2
    if abs(a - l) >= x and abs(a - r) >= x and abs(l - r) >= x:
        return 3
    return -1

t = int(input().strip())
results = []
for _ in range(t):
    l, r, x = map(int, input().strip().split())
    a, b = map(int, input().strip().split())
    results.append(min_operations(l, r, x, a, b))

print("\n".join(map(str, results)))
