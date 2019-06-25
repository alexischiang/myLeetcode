roma_dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    'IV':3,
    'IX':8,
    'XL':30,
    'XC':80,
    'CD':300,
    'CM':800
}
s = 'MCMXCIV'
# 遍历字符串时不需要强制转换为list
# 可直接使用enumerate
b = 0 
for i,n in enumerate(s):
    a = roma_dict.get(s[max(i-1,0):i+1],roma_dict[n])
    print(a)
    b += a

# 核心 dict.get(key, default=None)
# 有两位则返回两位对应 无则返回一位


print(b)

