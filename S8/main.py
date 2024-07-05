def add_file(file_name,n):
    with open(file_name, "w") as f:
        for i in range(n):
            f.write(input("name -> ")+" ")
            print("position?")

            print("1.Junior\n2.Middle\n3.Senior")
            num = int(input("-> "))
            match num:
                case 1: f.write("Junior ")
                case 2: f.write("Middle ")
                case 3: f.write("Senior ")
                case _: 
                    print("Error!") 
                    exit()

            f.write(input("salary -> ")+" ")
            f.write(input("bonus salary-> ")+" ")
            f.write(str(int(input("Which section (1-3)-> ")))+"-bo'lim\n")

####################################################################################

def best_workers(file_name):
    with open(file_name) as f:
        data = f.read().split("\n")[:-1]
    count1 = count2 = count3 = 0
    for i in range(len(data)):
        data[i] = data[i].split()
        data[i][-1] = data[i][-1].split("-")
        match data[i][-1][0]:
            case 1: count1 += 1 if float(data[i][-2]) > 0 else None
            case 2: count2 += 1 if float(data[i][-2]) > 0 else None
            case 3: count3 += 1 if float(data[i][-2]) > 0 else None
    if count1 == count2 == count3:
        print("1-Bo'lim\n2-Bo'lim\n3-Bo'lim")
    elif count1 > count2 > count3:
        print("1-Bo'lim")
    elif count1 < count2 > count3:
        print("2-Bo'lim")
    elif count1 < count2 < count3:
        print("3-Bo'lim")
    elif count1 == count2 > count3:
        print("1-Bo'lim\n2-Bo'lim")
    elif count1 < count2 == count3:
        print("2-Bo'lim\n3-Bo'lim")
    elif  count2 < count3 == count1:
        print("1-Bo'lim\n3-Bo'lim")

####################################################################################

n = int(input("Nechta malumot kiritmoqchisiz:"))
add_file("workers_data.txt",n)

best_workers("workers_data.txt")