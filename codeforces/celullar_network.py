"""
C. Cellular Network
time limit per test3 seconds
memory limit per test256 megabytes
You are given n points on the straight line — the positions (x-coordinates) of the cities and m points on the same line — the positions (x-coordinates) of the cellular towers. All towers work in the same way — they provide cellular network for all cities, which are located at the distance which is no more than r from this tower.

Your task is to find minimal r that each city has been provided by cellular network, i.e. for each city there is at least one cellular tower at the distance which is no more than r.

If r = 0 then a tower provides cellular network only for the point where it is located. One tower can provide cellular network for any number of cities, but all these cities must be at the distance which is no more than r from this tower.

Input
The first line contains two positive integers n and m (1 ≤ n, m ≤ 105) — the number of cities and the number of cellular towers.

The second line contains a sequence of n integers a1, a2, ..., an ( - 109 ≤ ai ≤ 109) — the coordinates of cities. It is allowed that there are any number of cities in the same point. All coordinates ai are given in non-decreasing order.

The third line contains a sequence of m integers b1, b2, ..., bm (- 109 ≤ bj ≤ 109) — the coordinates of cellular towers. It is allowed that there are any number of towers in the same point. All coordinates bj are given in non-decreasing order.

Output
Print minimal r so that each city will be covered by cellular network.

Examples
InputCopy
3 2
-2 2 4
-3 0
OutputCopy
4
InputCopy
5 3
1 5 10 14 17
4 11 15
OutputCopy
3
"""


from bisect import bisect_left


def minimum_r(n, m, cities, towers):
    # Sort cities and towers
    cities.sort()
    towers.sort()

    max_distance = 0  # To store the maximum of minimum distances

    # For each city, find the closest tower
    for city in cities:
        # Find the position to insert the city in the towers list
        idx = bisect_left(towers, city)

        # Calculate distances to the nearest towers
        left_distance = abs(city - towers[idx - 1]) if idx > 0 else float('inf')
        right_distance = abs(city - towers[idx]) if idx < len(towers) else float('inf')

        # Minimum distance for this city
        min_distance = min(left_distance, right_distance)

        # Update the maximum distance needed
        max_distance = max(max_distance, min_distance)

    return max_distance


# Input reading
n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

# Output the result
print(minimum_r(n, m, cities, towers))
