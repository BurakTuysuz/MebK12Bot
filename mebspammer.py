from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import threading as t
import requests
import os


def calistiralacaktarayici(browsername):
    low = browsername.lower()

    if low == 'chrome' or low == 'google' or low == 'googlechrome' or low == 'google chrome':
        return webdriver.Chrome()
    elif low == 'firefox':
        return webdriver.Firefox()
    elif low == 'edge':
        return webdriver.Edge()
    else:
        print("\n", "Lütfen yalnızca Google chrome, Firefox veya Edge Tarayıcısı'nın ismini girin")


def a(url, tarayici):
    try:
        while True:
            driver = calistiralacaktarayici(tarayici)
            driver.get(url)
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='begen' and "
                                                                                           "@onclick]")))
            button.click()
            driver.quit()

    except TimeoutException:
        print("\n", "Hata: Düğme bulunamadı veya zaman aşımı oldu")
    except Exception as e:
        print("\n", f"Hata Buton Bulunamadı: {str(e)}")


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
    if os.name == "posix":
        print('\n')
        tarayicial = input('Bilgisayarınızda Yüklü Olan Web Tarayıcınızın İsmini Girin (Google, Firefox, Edge): ')
        sor = input("Okul Sitesindeki İçerik Linkini Yapıştırın: ")
        try:
            al = requests.get(sor)
            if al.status_code == 200:
                sayi = int(
                    input("İşlem Aynı Anda Kaç Defa Yapılsın (Yüksek Sayı Bilgisayarın Donmasına Neden Olabilir, "
                          "Önerilen sayı: 5), (Açık olan programların kapatılması önerilir): "))
                threads = [t.Thread(target=a, args=(sor, tarayicial)) for _ in range(sayi)]

                for thread in threads:
                    thread.start()
            else:
                print("Geçersiz Site")

        except requests.exceptions.RequestException as e:
            print("\n", "Geçersiz Site: ", e)
            anakod()
        except Exception as ee:
            print("Hata: ", ee)

    else:
        print("İşletim Sisteminiz Yalnızca Linux Dağıtımı Olmalıdır")


if __name__ == '__main__':
    isim()
    anakod()
