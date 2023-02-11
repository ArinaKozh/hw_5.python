"""
Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя,
 если только для проверки вашего алгоритма.
на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
Например,

на входе
1+9/3*7-4
на выходе
18
"""

s = input()
s_a = []
for i in s:
    s_a.append(i)
print(s_a)


def calc(s_a, znak=None):
    if znak == None:
        i=0
        while True:
            if s_a[i] == "/":
                res = int(int(s_a[i-1])/int(s_a[i+1]))
                del s_a[i-1:i+2]
                s_a.insert(i-1,str(res))
            i+=1
            if i >= len(s_a)-1:
                calc(s_a,"*")
                break
    if znak == "*":
        i=0
        while True:
            if s_a[i] == "*":
                res = int(int(s_a[i-1])*int(s_a[i+1]))
                del s_a[i-1:i+2]
                s_a.insert(i-1,str(res))
            i+=1
            if i >= len(s_a)-1:
                calc(s_a,"+")
                break
    if znak == "+":
        i=0
        while True:
            if s_a[i] == "+":
                res = int(int(s_a[i-1])+int(s_a[i+1]))
                del s_a[i-1:i+2]
                s_a.insert(i-1,str(res))
            i+=1
            if i >= len(s_a)-1:
                calc(s_a,"-")
                break
    if znak == "-":
        i=0
        while True:
            if s_a[i] == "-":
                res = int(int(s_a[i-1])-int(s_a[i+1]))
                del s_a[i-1:i+2]
                s_a.insert(i-1,str(res))
            i+=1
            if i >= len(s_a)-1:
                break

    return(s_a[0])

print(calc(s_a))