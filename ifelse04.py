balans = 500_000
amount = float(input("Qancha pul yechmoqchisiz:"))

if amount >= 0:
    if amount <= balans:
        print("Pul yechildi.Qolgan balans x so'm")
       
    else:
     print(f"Mablag' yetarli emas.Sizning balansingiz: {balans} so'm.")

else:
   print("Manfiy summa kiritib bo'lmaydi.")

