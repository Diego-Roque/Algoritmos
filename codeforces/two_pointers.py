n = int(input())
t = int(input())

books = [int(input()) for _ in range(n)]

right = 0
left = 0
cur = 0
ans = 0

while left < n and right < n:
	# Finding the maximum right for which cur is less than t.
	while right < n:
		cur += books[right]
		right += 1

		# Subtracting the exceeded book from cur.
		if cur > t:
			right -= 1
			cur -= books[right]
			break

	ans = max(ans, right - left)
	cur -= books[left]
	left += 1

print(ans)