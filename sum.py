def summa():
    a=input('Введите числа: ').split()
    s=0
    print(a)
    for i in range(0, len(a)):
        a[i]=float(a[i])
        s+=a[i]
    print('сумма чисел: ',s)

def main():
    summa()
if __name__=='__main__':
    main()