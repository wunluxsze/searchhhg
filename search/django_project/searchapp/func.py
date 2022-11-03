import re

from django.conf.urls.static import static

#search_engine
# def search_sentence(search_word, file):
#     with open("static/"+file) as file: #Разбиение текста на предложения
#         text = re.split(r'[.|?|!]', file.read())
#     result = [] #создание списка
#     for sentence in text: #функция для прохождения по всему тексту
#         sentence = re.split('[' + re.escape(' ,0:@.-()/ ') + ']+', sentence) 
#         for word in sentence: 
#             if word.lower() == search_word:
#                 if sentence not in result:
#                     result.append(' '.join(sentence))
#     return set(result)

