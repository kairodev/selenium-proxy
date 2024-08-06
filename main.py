# coding: utf-8
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extension import proxies
from colorama import Fore, init
from random import choice
import os
import time

# Lista aleatoria de user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.37",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 YaBrowser/21.6.2.756 Yowser/2.5 Safari/537.36",
]

def abrir_navegador():
    chrome_options = webdriver.ChromeOptions()
    proxies_extension = proxies("voltz1020", "voltz1020_country-br", "geo.iproyal.com", "12321")
    chrome_options.add_extension(proxies_extension)
    chrome_options.add_argument(f'user-agent={choice(user_agents)}') # Randomização de user agent
    chrome_options.add_argument("--window-size=414,896")  # Tamano da tela
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(executable_path='./chromedriver.exe') # Localização do chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_script("window.navigator.chrome = {runtime: {}}")
    
    driver.delete_all_cookies()
    return driver

def efetuar_acao(driver, nome, telefone, sobrenome):
    maximo_tentativas = 5
    tentativas = 0
    sucesso = False
    while tentativas < maximo_tentativas and not sucesso:
        try:
            # Acessa o site
            driver.get('https://www.tribalwars.com.br/page/new')
            # Preenche o campo com id "register_username" usando xpath, aguarda o campo carregar até 25 segundos no maximo
            WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register_username"]'))).send_keys(nome)
            
            try:
                WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register_username"]')))
                print("SUCESSO")
                sucesso = True
                print(f'Nome: {nome}')
                driver.quit()
            except:
                print("NAO ENCONTRADO")
                sucesso = True
                print(f'Nome: {nome}')
                driver.quit()
            
            
            
            
        # Excessão realizada quando não encontra o elemento
        except NoSuchElementException as e:
            print(Fore.RED + f'Erro: {str(e)}')
        # Excessão realizada quando a internet está ruim, então ele tenta no maximo 5 vezes e vai para o próximo item da lista
        except TimeoutException as e:
            print(Fore.RED + f'Erro: {str(e)}')
            tentativas += 1
            print(f'Tentativa {tentativas} de {maximo_tentativas}')
            if tentativas == maximo_tentativas:
                print(Fore.RED + 'Número máximo de tentativas atingido. Não foi possível carregar a página.')

if __name__ == "__main__":
    
    # Ler a lista txt
    with open('lista.txt', 'r') as file:
        lines = file.readlines()
    
    #driver = abrir_navegador()
    
    # Para cada linha faz o procedimento
    for line in lines:
        nome, telefone, sobrenome = line.strip().split(':')
        driver = abrir_navegador()
        efetuar_acao(driver, nome, telefone, sobrenome)
    
    driver.quit()
