from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import threading as t
import requests
import os


def drivermain(link):
    driver = webdriver.Chrome()
    driver.get(link)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='begen' and "
                                                                                   "@onclick]")))
    return driver, button


def a(url):
    try:
        while True:
            driver, button = drivermain(url)
            button.click()
            driver.quit()
            drivermain(url)

    except TimeoutException:
        print("Hata: Düğme bulunamadı veya zaman aşımı oldu")


def isim():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTRED_EX)
    print(Style.BRIGHT)
    print("""
       ▄▄▄▄███▄▄▄▄      ▄████████ ▀█████████▄          ▄████████    ▄███████▄    ▄████████   ▄▄▄▄███▄▄▄▄     ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████ 
     ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███        ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
     ███   ███   ███   ███    █▀    ███    ███        ███    █▀    ███    ███   ███    ███ ███   ███   ███ ███   ███   ███   ███    █▀    ███    ███ 
     ███   ███   ███  ▄███▄▄▄      ▄███▄▄▄██▀         ███          ███    ███   ███    ███ ███   ███   ███ ███   ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
     ███   ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄       ▀███████████ ▀█████████▀  ▀███████████ ███   ███   ███ ███   ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
     ███   ███   ███   ███    █▄    ███    ██▄               ███   ███          ███    ███ ███   ███   ███ ███   ███   ███   ███    █▄  ▀███████████ 
     ███   ███   ███   ███    ███   ███    ███         ▄█    ███   ███          ███    ███ ███   ███   ███ ███   ███   ███   ███    ███   ███    ███ 
      ▀█   ███   █▀    ██████████ ▄█████████▀        ▄████████▀   ▄████▀        ███    █▀   ▀█   ███   █▀   ▀█   ███   █▀    ██████████   ███    ███ 
                                                                                                                                          ███    ███ 


                                                            İşlemi Durdurmak İçin Programı Kapatın
    """)


def anakod():
    print('\n')
    sor = input("Okul Sitesindeki İçerik Linkini Yapıştırın: ")
    try:
        al = requests.get(sor)
        if al.status_code == 200:
            sayi = int(
                input("İşlem Aynı Anda Kaç Defa Yapılsın (Yüksek Sayı Bilgisayarın Donmasına Neden Olabilir): "))
            threads = [t.Thread(target=a, args=(sor,)) for _ in range(sayi)]

            for thread in threads:
                thread.start()
        else:
            print("Geçersiz Site")
            anakod()

    except requests.exceptions.RequestException as e:
        print("Geçersiz Site: ", e)
        anakod()


if __name__ == '__main__':
    isim()
    anakod()
