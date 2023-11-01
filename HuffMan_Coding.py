#Получаем на вход текстовый файл. Пока не знаем для кодирования или декодирования
input_text= "jfhfyehfbskwurbrbdhdhddyweygb" 
#Создаём массив частотности встречи каждого символа
frequency = {}
#Заполняем этот массив 
for i in input_text: 
    if i in frequency:
        frequency[i]+=1
    else: 
        frequency[i]=1   

#Проверяем вывод
print(frequency)


''' Нам нужно отсортировать по возрастанию частотности
Варианты из stack overflow
dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
for i in sorted(frequency, key=frequency.get, reverse=True):
    print(i, frequency[i])'''


#Отсортируем по частотности от самого редкого к самому частому 
frequency=dict(sorted(frequency.items(), key=lambda item: item[1]))

print(frequency)