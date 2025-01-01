from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import threading as t
import requests
import os


def a(url):
    try:
        while True:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
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
    os.system('clear')
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


    """)


def anakod():
    sor = input("Okul Sitesindeki Icerik Linkini Yapıstırın: ")
    try:
        al = requests.get(sor)
        if al.status_code == 200:
            sayi = int(input("Islem Ayni Anda Kac Defa Yapilsin - Yüksek Sayi Sorun Yaratabilir, Önerilen sayi: 10, (Lütfen Acik olan programlari kapatin): "))
            threads = [t.Thread(target=a, args=(sor,)) for _ in range(sayi)]
            print("Goruntulenme ve begeni saglaniyor. Sonlandirmak icin yazilimi kapatin")
            for thread in threads:
                thread.start()
        else:
            print("Geçersiz Link. Örnek link: https://okul.meb.k12.tr/icerikler/icerik_sayfasi.html")

    except requests.exceptions.RequestException as e:
        print("\n", "Geçersiz Site: ", e)
        anakod()


if __name__ == '__main__':
    isim()
    anakod()
