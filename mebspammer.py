from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import threading as t
import requests
import os


def a(url):
    try:
        while True:
            driver = webdriver.Edge()
            driver.get(url)
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='begen' and "
                                                                                           "@onclick]")))
            button.click()
            driver.quit()

    except TimeoutException:
        print("\n", "Hata: Zaman aşımı oldu")
    except Exception as e:
        print("\n", f"Hata: {str(e)}")


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
                input("İşlem Aynı Anda Kaç Defa Yapılsın (Yüksek Sayı Donmaya Neden Olabilir, "
                      "Önerilen sayı: 5), (Lütfen Açık olan programları kapatın): "))
            threads = [t.Thread(target=a, args=(sor)) for _ in range(sayi)]

            for thread in threads:
                thread.start()
        else:
            print("Geçersiz Link. Örnek link: https://okul.meb.k12.tr/icerikler/icerik_sayfasi.html")

    except requests.exceptions.RequestException as e:
        print("\n", "Geçersiz Site: ", e)
        anakod()
    except Exception as ee:
        print("Hata: ", ee)



if __name__ == '__main__':
    isim()
    anakod()
