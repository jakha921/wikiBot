import wikipedia

wikipedia.set_lang("ru")

# print(wikipedia.search('Марс'))
# print(wikipedia.summary('Марс'))
# print(wikipedia.page('Марс'))


while True:
    searched = input("Что ищем? ")    
    
    if searched:
        print(wikipedia.summary(searched))
        
        stop = input("Еще? \nДА/НЕТ: ").lower()
        if stop == "нет":
            break
    else:
        print("Не нашел нечего")
    
    