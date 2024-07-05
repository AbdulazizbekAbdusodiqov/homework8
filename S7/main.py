def draws(dct: dict):
    lst_0 = []
    lst_1 = []

    for key, val in dct.items(): #ishim yengillashishi uchun 0 larni alohida 1 larni alohida listga sovoldim
        if val:
            lst_1.append(key)
        else:
            lst_0.append(key)

    if len(lst_1) == len(lst_0): #0 va 1 lar soni teng bolgan xolatlarda
        print("0")
        print(", ".join(lst_0))     
        print("1")
        print(", ".join(lst_1))     
    elif len(lst_1) > len(lst_0): #1 lar soni katta bolganda
        print("1")
        print(", ".join(lst_1))     
    else:                         #0 lar soni katta bolganda
        print("0")
        print(", ".join(lst_0))     

######################################################################

n = int(input("n="))
dct = {input("ism->" ) : int(input("1 or 0 ->")) for  i in range(n)} #bir qatorli forda qilindi
draws(dct)