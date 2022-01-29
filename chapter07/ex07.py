def calsum(n):
    """1~n까지의 합계를 구해 리턴한다."""
    total = 0
    for i in range(n+1):
        total += i
    return total

# help(calsum)

print(calsum(10))
