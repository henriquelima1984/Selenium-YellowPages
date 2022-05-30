from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import json

#Aqui nós vamos abrir nosso arquivo data.json e vamos escrever nele "w".
with open("data.json", "w") as f:
    json.dump([], f)

#Função criada para ler e salvar nossos dados em um dicionário .json
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data) 
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#Aqui criamos uma variável chamada options para instânciar a classe ChromeOptions()
options = webdriver.ChromeOptions()
#A primeira opção resolve o erro do bluetooth, caso seu pc não tenha adicione essa linha.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#Configurando o projeto para abrir em tela cheia.
options.add_argument('start-maximized')

#Aqui iniciamos o trabalho, passe suas options.
browser = webdriver.Chrome(options=options)

open_website = browser.get("https://www.yellowpages.com/")

input1 = browser.find_element(By.NAME, 'search_terms')
input1.click()
input1.send_keys('restaurant')

sleep(2)

input2 = browser.find_element(By.NAME, 'geo_location_terms')
input2.click()
input2.send_keys('Toronto, OH')

sleep(2)

search_buttom = browser.find_element(By.TAG_NAME, 'button')
search_buttom.click()

sleep(2)

list_of_restaurants = browser.find_elements(By.CLASS_NAME, 'v-card')

#print(len(list_of_restaurants))

sleep(5)

#Aqui criamos às variáveis que vamos utilizar no nosso arquivo data.json
restaurant_name = ''
address = ''
link = ''

# vamos iterar sobre os itens que estão dentro de v-card e pegar nome, endereço e o link do website.
for restaurant in list_of_restaurants:
    try:
        restaurant_name = restaurant.find_element(By.CLASS_NAME, 'business-name').text
        #print(restaurant_name.text)
        address = restaurant.find_element(By.CLASS_NAME, 'street-address').text
        #print(address.text)
        link = restaurant.find_element(By.CLASS_NAME, 'track-visit-website').get_attribute('href')
        #print(link)
    except:
        pass

    write_json({
       "restaurant": restaurant_name,
       "adress": address,
       "website": link
    })
