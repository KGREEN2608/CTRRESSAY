import rsa
#Tính ước chung lớn nhất
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# Mã hóa tin nhắn
def mahoa(h, e, n):
    m = pow(h, e, n)
    return m
 
# Giải mã tin nhắn
def giaima(c, d, n):
    g = pow(c, d, n)
    return g
#Message cần mã hóa và giải mã
message = "Discrete Structure"
#Áp dụng công thức
p = 5
q = 7
n = p * q
phi = (p - 1) * (q - 1)
#Tạo cặp khóa public và private
publicKey, privateKey = rsa.newkeys(1024)
#Chạy chương trình
encMessage = rsa.encrypt(message.encode(),publicKey)
print("Tin nhắn: ",message)
print("Mã hóa tin nhắn: ",encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("Giải mã tin nhắn: ",decMessage)
