# coding: utf-8
import heapq
from os.path import abspath 

def build_Huffman_tree(freq):
    tree = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(tree)
                   
    while len(tree) > 1:
        son_1 = heapq.heappop(tree)
        son_2 = heapq.heappop(tree)
                
        for code_inf in son_1[1:]:
                code_inf[1]='0' + code_inf[1]
                
        for code_inf in son_2[1:]:
                code_inf[1]='1' + code_inf[1]
        total=son_1[0]+ son_2[0]
        heapq.heappush(tree, [total] + son_1[1:] + son_2[1:])
        root= tree[0] 
    return root

def create_huffman_codes(huffman_tree):
    huffman_codes = {}
    for code_inf in huffman_tree[1:]:
        ch , code = code_inf
        huffman_codes[ch]= code
    with open('HuffmanCodes.py', 'w+', encoding='UTF-8') as f:
        f.write('SavedHuffmanCodes = '+str(huffman_codes))
    return huffman_codes

def encoding(input_text , huffman_codes):
    encoded_text = ""
    for ch in input_text:
        encoded_text += huffman_codes[ch]
    return encoded_text

def decoding(encoded_text, huffman_codes):
    decoded_text = ""

    huffman_decodes= {}
    for ch , code in huffman_codes.items():
        huffman_decodes[code]= ch
        
    temp = ""
    for binary_digit in encoded_text:
        temp += binary_digit
        if temp in huffman_decodes:
            decoded_text+= huffman_decodes[temp]
            temp = ""
            
    return decoded_text

def main():
    
    #Получаем на вход текстовый файл. Пока не знаем для кодирования или декодирования
    mode = int(input("В каком режиме запустить программу? 1- кодирование, 2 - декодирование"))
    if(mode==1):
        try:
            txt = input("Введите полный путь к файлу, с которым хотите работать: ")
            file = open(txt,encoding='utf-8',mode= "r")
            input_text= file.read()
        except FileNotFoundError:
            print("Ошибка: Файл не найден")  
        #Создаём массив частотности встречи каждого символа
        file.close()
        frequency = {}
        #Заполняем этот массив 
        for i in input_text: 
            if i in frequency:
                frequency[i]+=1
            else: 
                frequency[i]=1 
        huffman_tree = build_Huffman_tree(frequency)
        huffman_codes = create_huffman_codes(huffman_tree)
        encoded_text = encoding(input_text, huffman_codes)
        with open('encoded_text.txt', 'w+', encoding='UTF-8') as out:
            out.write(encoded_text) 
            print("Закодированный текст находится в файле: ", abspath("encoded_text.txt"))
        
    if(mode==2):
        with open('encoded_text.txt', 'r',encoding='UTF-8') as inp:
            input_text=inp.read()
        from HuffmanCodes import SavedHuffmanCodes
        decoded_text = decoding(input_text, SavedHuffmanCodes)
        with open('decoded_text.txt', 'w+') as out:
            out.write(decoded_text)
            print("Декодированный текст находится в файле: ", abspath("decoded_text.txt"))

main()






