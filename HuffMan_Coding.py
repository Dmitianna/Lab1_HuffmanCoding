#Для построения дерева понадобятся элементы, из которых мы будем его собирать 
class HuffNode(object):  
    def __init__(self , left = None , right = None , root = None):
        self.left= left
        self.right= right 
        self.root = root
    def children(self):
        return(self.left, self.right)

    
#Получаем на вход текстовый файл. Пока не знаем для кодирования или декодирования
try:
    txt = input("Введите полный путь к файлу, с которым хотите работать: ")
    file = open(txt,encoding='utf-8',mode= "r")
    input_text= file.read()
except FileNotFoundError:
    print("Ошибка: Файл не найден")
#Создаём массив частотности встречи каждого символа
frequency = {}
#Заполняем этот массив 
for ch in input_text: 
    if ch in frequency:
        frequency[ch]+=1
    else: 
        frequency[ch]=1   
''' Нам нужно отсортировать по возрастанию частотности
Варианты из stack overflow
dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
for i in sorted(frequency, key=frequency.get, reverse=True):
    print(i, frequency[i])'''

#Отсортируем по частотности от самого редкого к самому частому 
freq=dict(sorted(frequency.items(), key=lambda item: item[1]))
print(freq)
#Для удобства работы преобразуем в список кортежей 
frequency= [(fr,ch) for ch,fr in freq.items()]
print(frequency)

