def even():
    s=int(input('Введите число: '))
    if s%2==0:
        print(s, ' - чётное')
    else:
        print(s, ' - нечётное')
def main():
    even()
if __name__=='__main__':
    main()