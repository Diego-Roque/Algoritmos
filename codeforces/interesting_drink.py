"""
B. Interesting drink
time limit per test2 seconds
memory limit per test256 megabytes
Vasiliy likes to rest after a hard work, so you may often meet him in some bar nearby. As all programmers do, he loves the famous drink "Beecola", which can be bought in n different shops in the city. It's known that the price of one bottle in the shop i is equal to xi coins.

Vasiliy plans to buy his favorite drink for q consecutive days. He knows, that on the i-th day he will be able to spent mi coins. Now, for each of the days he want to know in how many different shops he can buy a bottle of "Beecola".

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of shops in the city that sell Vasiliy's favourite drink.

The second line contains n integers xi (1 ≤ x_i ≤ 100 000) — prices of the bottles of the drink in the i-th shop.

The third line contains a single integer q (1 ≤ q ≤ 100 000) — the number of days Vasiliy plans to buy the drink.

Then follow q lines each containing one integer mi (1 ≤ mi ≤ 109) — the number of coins Vasiliy can spent on the i-th day.

Output
Print q integers. The i-th of them should be equal to the number of shops where Vasiliy will be able to buy a bottle of the drink on the i-th day.

"""

import bisect

# Input reading
n = int(input())  # Number of shops
shop_prices = list(map(int, input().split()))  # Prices of drinks in the shops
q = int(input())  # Number of days
queries = [int(input()) for _ in range(q)]  # Budgets for each day

shop_prices.sort()

# Process each query
results = []
for budget in queries:
    # Use bisect_right to find the number of shops Vasiliy can afford
    affordable_shops = bisect.bisect_right(shop_prices, budget)
    results.append(affordable_shops)

# Output results
print("\n".join(map(str, results)))
