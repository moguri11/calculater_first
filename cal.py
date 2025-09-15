from f_multiple import f_multiple
from f_divided import f_divided
from f_add import f_add
from f_substract import f_substract

A, B = map(int, input().strip())
cal = input()

if cal == "곱셈":
    print(f_multiple(A, B))
elif cal == "나눗셈":
    print(f_divided(A, B))
elif cal == "덧삼":
    print(f_add(A, B))
else :
    print(f_substract(A, B))

