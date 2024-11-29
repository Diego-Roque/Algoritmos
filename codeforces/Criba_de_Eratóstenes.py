ans = []
for _ in range(int(input())):
	div_num = 0
	x = int(input())
	i = 1
	while i * i <= x:
		if x % i == 0:
			div_num += 1 if i**2 == x else 2
		i += 1
	ans.append(div_num)

print("\n".join(str(i) for i in ans))