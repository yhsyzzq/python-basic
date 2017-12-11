s = "hello zzq"

print(str(s))

print(repr(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3),repr(x*x*x).rjust(6))

num = "12"
print(num.zfill(5))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{1} and {0}'.format('知名','传参'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
