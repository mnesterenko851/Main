def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

print(sum_recursive(15))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(56, 26))


def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

print(is_palindrome("radar"))


def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
    else:
        for i in range(len(s)):
            permute(s[:i] + s[i+1:], answer + s[i])

permute("aбв")