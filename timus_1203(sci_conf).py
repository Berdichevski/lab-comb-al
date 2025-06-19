num = int(input())
conferences = []

for i in range(num):
    start, end = map(int, input().split())
    conferences.append((start, end))

conferences.sort(key=lambda x: x[1])

visited_count = 0
current_time = 0

for start, end in conferences:
    if start > current_time:
        visited_count += 1
        current_time = end

print(visited_count)
