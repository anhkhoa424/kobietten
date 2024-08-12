# bài1:
number = int(input("mời bạn nhập vào một số nguyên"))
if number % 2 == 0:
    print(number,"là số chẵn")
else:
    print(number,"là số lẻ")

# bài2:
N = int(input("Nhập mộy số nguyên dương N:"))
if N < 1:
    print("không hợp lệ")
else:
    i = 1
    while i <= N:
        print(i)
        i +=1
# bài3:
N = int(input("Nhập một nguyên dương N:"))
if N < 1:
    print("không hợp lệ")
else:
    total = 0
    i = 1
    while i <= N:
        total +=i
        i += 1
    print("tổng các số từ 1 đến", N, "là:", total)

n=int(input("Mời bạn nhập vào 1 số để tính bảng cửu chương"))
i=1
while(i<=10):
    print(n,"X",i,"=",n*i)
    i+=1
#bai 5
    n=input("mời bạn nhập số chẵn")
    print(n,'đây là số chẵn')
    tong = n + n
    print(tong)