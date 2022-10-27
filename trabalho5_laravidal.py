import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

print("Imports feitos")


# SITE 1
page1 = "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html"
html = requests.get(page1).text
soup1 = BeautifulSoup(html, "html.parser")
 
text_array1 = []
get = soup1.find_all('p')
text_dir1 = list(get)

for text in text_dir1:
    text_array1.append(text.get_text().split(" "))

# Removendo as palavras repetidas dentro do site 1

all1 = []
for i in text_array1:
  for j in i:
    all1.append(j)

vocab1 = []

contador = 0

for word in all1:
    if word not in vocab1:
        vocab1.append(word)
        contador += all1.count(word)
    contador = 0
    
    
    
# SITE 2
page2 = "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"
html = requests.get(page2).text
soup2 = BeautifulSoup(html, "html.parser")
 
text_array2 = []
get = soup2.find_all('p')
text_dir2 = list(get)

for text in text_dir2:
    text_array2.append(text.get_text().split(" "))

# Removendo as palavras repetidas dentro do site 2

all2 = []
for i in text_array2:
  for j in i:
    all2.append(j)

vocab2 = []
contador = 0

for word in all2:
    if word not in vocab2:
        vocab2.append(word)
        contador += all2.count(word)
    contador = 0
    
    
    # SITE 3
page3 = "https://hbr.org/2022/04/the-power-of-natural-language-processing"
html = requests.get(page3).text
soup3 = BeautifulSoup(html, "html.parser")
 
text_array3 = []
get = soup3.find_all('p')
text_dir3 = list(get)

for text in text_dir3:
    text_array3.append(text.get_text().split(" "))

# Removendo as palavras repetidas dentro do site 3

all3 = []
for i in text_array3:
  for j in i:
    all3.append(j)

vocab3 = []
contador = 0

for word in all3:
    if word not in vocab3:
        vocab3.append(word)
        contador += all3.count(word)
    contador = 0
    
    
    # SITE 4
page4 = "https://monkeylearn.com/natural-language-processing/"
html = requests.get(page4).text
soup4 = BeautifulSoup(html, "html.parser")
 
text_array4 = []
get = soup4.find_all('p')
text_dir4 = list(get)

for text in text_dir4:
    text_array4.append(text.get_text().split(" "))

# Removendo as palavras repetidas dentro do site 4

all4 = []
for i in text_array4:
  for j in i:
    all4.append(j)

vocab4 = []
contador = 0

for word in all4:
    if word not in vocab4:
        vocab4.append(word)
        contador += all4.count(word)
    contador = 0
    
    
    # SITE 5
page5 = "https://www.tableau.com/learn/articles/natural-language-processing-examples"
html = requests.get(page5).text
soup5 = BeautifulSoup(html, "html.parser")
 
text_array5 = []
get = soup5.find_all('p')
text_dir5 = list(get)

for text in text_dir5:
    text_array5.append(text.get_text().split(" "))

# Removendo as palavras repetidas dentro do site 5

all5 = []
for i in text_array5:
  for j in i:
    all5.append(j)

vocab5 = []
contador = 0

for word in all5:
    if word not in vocab5:
        vocab5.append(word)
        contador += all5.count(word)
    contador = 0
    
    
    # Adicionando os lexemas de todos os sites, sem repetições 
all_texts = []
vocabSites = [vocab1, vocab2, vocab3, vocab4, vocab5]

for site in vocabSites:
  for word in site:
      if word not in all_texts:
          all_texts.append(word)

# Calculando a frequência que cada palavra de todos os sites aparece em cada site individualmente
wordFreq1 = []
wordFreq2 = []
wordFreq3 = []
wordFreq4 = []
wordFreq5 = []
contador = 0

for word in all_texts:
    contador += all1.count(word)
    wordFreq1.append(contador)
    contador = 0

for word in all_texts:
    contador += all2.count(word)
    wordFreq2.append(contador)
    contador = 0
  
for word in all_texts:
    contador += all3.count(word)
    wordFreq3.append(contador)
    contador = 0

for word in all_texts:
    contador += all4.count(word)
    wordFreq4.append(contador)
    contador = 0

for word in all_texts:
    contador += all5.count(word)
    wordFreq5.append(contador)
    contador = 0
    
    
    # Criando a tabela com a biblioteca pandas
from google.colab.data_table import DataTable
DataTable.max_columns = 2945

linha1 = pd.Series({all_texts[i]: wordFreq1[i] for i in range(len(all_texts))})
linha2 = pd.Series({all_texts[i]: wordFreq2[i] for i in range(len(all_texts))})
linha3 = pd.Series({all_texts[i]: wordFreq3[i] for i in range(len(all_texts))})
linha4 = pd.Series({all_texts[i]: wordFreq4[i] for i in range(len(all_texts))})
linha5 = pd.Series({all_texts[i]: wordFreq5[i] for i in range(len(all_texts))})

df = pd.DataFrame([linha1, linha2, linha3, linha4, linha5])
df.index = np.arange(1, len(df) + 1)
df.index.names = ['DOCUMENTOS']
df
