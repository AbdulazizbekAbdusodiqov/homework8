def split_separate_line(lst):
    print("=================")
    for i in range(len(lst)-1): #indexerror bolmasligi uchun
        if lst[i] == lst[i+1]-1 or lst[i] == lst[i+1]+1:
            print(lst[i], lst[i+1])

########################################################################

n = int(input("n= "))
lst = [int(input(f"{i+1}->")) for i in range(n)]

split_separate_line(lst)