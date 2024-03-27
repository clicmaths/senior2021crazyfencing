n = int(input())
h = list(map(float, input().split("")))
b = list(map(float, input().split("")))
aire = float(0)

for i in range(n):
    aire += (b[i]*(h[i] + h[i+1]))/2

print(aire)