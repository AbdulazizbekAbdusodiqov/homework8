def My_sort(lst):
    return sorted(lst, key=lambda x: my_sum(x))

#####################################################

def my_sum(x):
    sum = 0
    if x == 0:
        return 0
    if x > 0:
        for i in str(x):
            sum += int(i)
    else:
        for i in str(x)[1:]:
            sum += int(i)
    return sum

#####################################################
n = int(input("n= "))

lst = [int(input(f"{i+1}->")) for i in range(n)]
lst = My_sort(lst)

print(lst)
