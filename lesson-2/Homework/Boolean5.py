# Create a program that accepts two strings and checks if they have the same length.

matn1 = str(input("Enter the first strig: "))
matn2 = str(input("Enter the second string: "))

leng1 = len(matn1)
leng2 = len(matn2)

if leng1 == leng2:
    print(f"{matn1} so'zining uzunligi {matn2} so'zining uzunligi bilan teng")
else:
    print(f"{matn1} va {matn2}larning uzunliklari har xil.")