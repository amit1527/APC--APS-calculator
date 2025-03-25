print("shall we start? type 'yes' :", end = "")
y = input()
if y == "yes":
    print("your monthly income:", end = "")
    inc = int(input())
    print("your monthly consumption:", end = "")
    con = int(input())
    APC = con/inc
    print("Your APC :",APC)

    p =print("Wanna know yout APS? type 'yes' :", end = "")
    aps = input()
    if aps == "yes":
        APS = 1-APC
        print("Your APS :", APS)
    else:
        print(p,aps)
else:
    print("shall we start? type 'yes' :", end = "")
    y = input()


