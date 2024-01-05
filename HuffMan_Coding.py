import heapq
from heapq import heappush, heappop
import ast 
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
    #меьшая частотность -> приоритет обработки 
    def __lt__(self, other):
          return self.freq < other.freq


def buildHuffmanTree(input_text):
    # Базовый случай: пустая строка
    if len(input_text) == 0:
        return('ce la vie, тут работать не с чем :()')
    #Создаём словарь частотности встречи каждого символа
    freq = {}
    #Заполняем  
    for ch in input_text: 
        if ch in freq:
            freq[ch]+=1
        else: 
            freq[ch]=1    
    #Отсортируем по частотности от самого редкого к самому частому 
    freq=dict(sorted(freq.items(), key=lambda item: item[1]))
    print(freq)
    #Для удобства работы преобразуем в список  
    freq = [Node(fr,ch) for fr,ch in freq.items()]
    #преобразовываем данные в структуру кучи
    heapq.heapify(freq)
    #пока не получим один узел
    while len(freq) != 1:
        #Удаляем два узла с наименьшей частотой
        left = heappop(freq)
        right = heappop(freq)
        # создаем узел с суммарным значением удаленных частот и вставляем в кучу,чтобы структура не нарушилась
        total = left.freq + right.freq
        heappush(freq, Node(None, total, left, right))
    # root - корень
    root = freq[0]
    # проходит по дереву Хаффмана и сохраняет коды Хаффмана в словаре.
    huffmanCode = {}
    encode(root,'', huffmanCode)
    print(huffmanCode)
    with open('HuffmanCodes.txt','w+',encoding='utf-8') as out:
        for key,val in huffmanCode.items():
            out.write('{}:{}\n'.format(key,val))
    return huffmanCode


def islast(item):
    return (item.left is None and item.right is None)

def encode(root, s, huffman_code):
    if root is None:
        return("Дерево не построено")
    # обнаружил листовой узел
    if islast(root):
        if len(s) > 0:
            huffman_code[root.ch] = s;
        else:
            huffman_code[root.ch] = '1';
    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)

def decode(root, index, s):
    if root is None:
        return index
    # обнаружил листовой узел
    if islast(root):
        print(root.ch, end='')
        return index
    index = index + 1
    if s[index] == '0':
        root = root.left  
    else:
        root.right
    return decode(root, index, s)   

def encoding_text(huffmanCode, input_text):
    encoded = ''
    for ch in input_text:
        encoded += huffmanCode.get(ch)
    print('The encoded string is:', encoded)


def decoding_text(huffmanCode, input_text,s):
    print('The decoded string is:', end=' ')
    index = -1
    while index < len(s) - 1:
        index = decode(root, index, s)


if __name__ == '__main__':
    #Получаем на вход текстовый файл. Пока не знаем для кодирования или декодирования
    try:
        txt = input("Введите полный путь к файлу, с которым хотите работать: ")
        file = open(txt,encoding='utf-8',mode= "r")
        input_text= file.read()
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    print(input_text)
    mode= int(input(" В каком режиме запустить программу? 1-закодировать , 2 - декодировать"))
if mode==1:
    encoding_text(buildHuffmanTree(input_text),input_text)
if mode==2:
    decoding_text(buildHuffmanTree(input_text), input_text)
file.close()