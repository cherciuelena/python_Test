for i in range(10):
    print(f'Set instructiuni [{i + 1}]')

def get_sum(n):
    if n == 0:
        return 0
    
    return n + get_sum(n-1)

print(get_sum(7))