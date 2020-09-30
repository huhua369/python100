# print(0b100)
# print(0o100)
# print(100)
# print(0x100)

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d'%(a, b, a + b))
# print('%d - %d = %d'%(a, b, a - b))
# print('%d * %d = %d'%(a, b, a * b))
# print('%d / %d = %d'%(a, b, a / b))
# print('%d // %d = %d'%(a, b, a // b))
# print('%d %% %d = %d'%(a, b, a % b))
# print('%d ** %d = %d'%(a, b, a ** b))

# a = 10
# b = 3
# a += b
# a *= a + 2
# print(a)
#输入年份判断是不是闰年
year = int(input('请输入年份：'))

is_leap = year%4 == 0 and year%100 != 0 or year%400 == 0
print(is_leap)