chipta = 100

yosh = int(input("Yoshingizni kiriting:"))

if yosh < 7:
    chipta *= 0.5

if yosh >= 7 and yosh <= 17:
    chipta *= 0.8

if yosh > 60 :
    chipta *= 0.7

print("chipta narxi:" , chipta)
    