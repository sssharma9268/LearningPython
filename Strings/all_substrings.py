str = "abcd"
n = len(str)


def all_substrings(str, n):
    res = [str[i:j] for i in range(n) for j in range(i + 1, n+1)]
    print(res)


all_substrings(str, n)