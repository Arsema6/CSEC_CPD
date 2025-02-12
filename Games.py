def guest_uniform(n, uniforms):
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if uniforms[i][0] == uniforms[j][1]:
                    count += 1
    return count
n = int(input())
uniforms = [tuple(map(int, input().split())) for _ in range(n)]
print(guest_uniform(n, uniforms))
