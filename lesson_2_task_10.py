
def bank(x, y):

    return x*((1.1)**y) 

print('Введите сумму: ')
x = int(input())
print('Введите срок: ')
y = int(input())
print(f'Итоговая сумма: {bank(x,y)}')
