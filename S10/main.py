def colors_time(lst):
    count = len(lst)*2
    for i in range(len(lst)-1):
        lst[i] = lst[i]
        if not lst[i] == lst[i+1] :
            count += 1
    return count

n = int(input("n= "))

lst = [input(f"{i+1}-rang -> ").capitalize() for i in range(n)]
count = colors_time(lst)

print(count)