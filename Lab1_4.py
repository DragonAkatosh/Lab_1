'''
Вправа 4
Дано рядок, що складається з рівно двох слів, розділених пропуском. 
Надрукуйте новий рядок, у якому позиції першого та другого слова змінені (друге слово друкується спочатку).
У завданні не можна використовувати цикли і вказівку «якщо».

Токар Іван
'''
s = input("Enter a string: ")
words = s.split(' ')
print (words[1] + ' ' + words[0])
