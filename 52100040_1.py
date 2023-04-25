def gcd(a, b):

    if b == 0:
        return a, 1, 0
    else:
        u, s, t = gcd(b, a % b)
        return u, t, s - (a // b) * t
def inverseMod(a, m):
    u, s, _  = gcd(a, m)
    if u != 1:
        return None  #Trả về trong trường hợp ko tồn tại inverse
    else:
        return s % m

print("Kết quả:",inverseMod(60,11))