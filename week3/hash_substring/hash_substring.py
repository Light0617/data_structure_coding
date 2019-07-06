# python3
import random
def read_input():
    # return (raw_input().rstrip(), raw_input().rstrip())
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(pattern, p, x):
    ans = 0
    for c in pattern:
        ans = (ans * x + ord(c)) % p
    return ans
def multiple(x, p, length):
    result = [0] * (length + 1)
    prod = 1
    for i in range(length):
        prod = (prod * x) % p 
        result[i + 1] = prod
    return result

def rabin_karp(text, pattern):
    p = 1000000007
    x = random.randrange(1, p)
    prods = multiple(x, p, len(pattern))
    result = []

    p_hash, t_hash = poly_hash(pattern, p, x), 0
    for i in range(len(text) - len(pattern), -1, -1):
        if i == len(text) - len(pattern):
            t_hash = poly_hash(text[i : i + len(pattern)], p, x)
        else:
            t_hash = (x * t_hash % p) - (ord(text[i + len(pattern)]) * prods[len(pattern)] % p) + ord(text[i])
            t_hash %= p
        if p_hash != t_hash:
            continue
        if pattern == text[i : i + len(pattern)]:
            result.append(i)
    return result

def get_occurrences(pattern, text):
    print(pattern, text)
    return rabin_karp(text, pattern)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

