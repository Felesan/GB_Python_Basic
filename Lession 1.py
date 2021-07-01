# Lession 1

# Task 1 ---
a = 1
b = 1.1
print('Тест:', a, b)
q1 = input('Введите число - ')
q2 = input('Введите слово - ')
print('Ваш выбор:', q1, q2)

# Task 2 ---
s = int(input('Введите время в секундах: '))
def hms(s):
    h = s // 3600
    m = s % 3600 // 60
    s = s % 3600 % 60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
print(hms(s))

# Task 3 ---
n = int(input("Введите число n: "))
nt = str(n)
nt1 = nt + nt
nt2 = nt + nt + nt
ans = n + int(nt1) + int(nt2)
print("Результат n + nn + nnn:", ans)

# Task 4 ---
num = int(input('Введите число: '))
mnum = num%10
number = num//10
while num > 0:
    if num%10 > mnum:
        mnum = num%10
    number = num//10
print('Наибольшая цифра в числе: ', mnum)

# Task 5 ---
v = int(input('Введите выручку фирмы: '))
z = int(input('Введите издержки фирмы: '))
if v >= z:
    print('Фирма работает в прибыль =)')
    r = v / z
    print('Рентабельность выручки:', "%.2f" % r)
    s = int(input('Введите количество сотрудников фирмы: '))
    c = v / s
    print('Прибыль на одного сотрудника:', "%.2f" % c)
else: print('Фирмы работает в убыток =(')

# Task 6 ---
s = int(input('Введите результат первого дня, км.:'))
t = int(input('Введите целевой результат, км.:'))
i = 1
while s < t:
    s *= 1.1
    i += 1
print('При прогрессе в 10% вы достигнете цели через', i, 'дней!')