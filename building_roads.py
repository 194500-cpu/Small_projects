import sys
import collections

cities, roads = map(int, sys.stdin.readline().strip().split())
visited = [False for node in range(cities + 1)]
adj_list = [list() for node in range(cities + 1)]
groups = 0
group_points = []

for road in range(roads):
    city1, city2 = map(int, sys.stdin.readline().strip().split())
    adj_list[city1].append(city2)
    adj_list[city2].append(city1)


for i in range(1, cities + 1):

    if not visited[i]:
        group_points.append(i)
        groups += 1
    stack = collections.deque([i])

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
        for neighbor  in reversed(adj_list[node]):
            if not visited[neighbor]:
                stack.append(neighbor)

if len(group_points) < 1:
    print("0")
else:
    print(len(group_points)-1)
    for point in range(len(group_points)-1):
        print(group_points[point], group_points[point + 1])