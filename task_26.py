"""
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""
A = int(input("Введите число "))
B = int(input("Введите степень "))

def step(A,B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return step(A, B-1)*A

print(step(A,B))