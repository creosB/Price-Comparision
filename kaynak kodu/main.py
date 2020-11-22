import requests
import sys
import ssl
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
import tkinter as tk
import webbrowser
import tkinter.font as tkFont

def migros():
    il = giris.get()
    yazi6.config(text="Migros metin belgesine yazdırıldı.")
    m = ["https://www.migros.com.tr/cubuk-tursusu-kg-p-121ec19",
         "https://www.migros.com.tr/pringles-original-sade-70-g-p-4da8c2"]
    a = il + ".txt"
    f = open(a,"w+")
    yazi.config(text="Dosya adı: %s" % il)

    for links in m:
        def sembolleritemizle(fiyatlar):
            sembolsuzkelime = []
            semboller = "[]''tl"
            for kelime in fiyatlar:
                for sembol in semboller:
                    if sembol in kelime:
                        kelime = kelime.replace(sembol, "")

                if (len(kelime) > 0):
                    sembolsuzkelime.append(kelime)
            return sembolsuzkelime

        def yazitemizle(adlar):
            sembolsuzad = []
            sems = "[]''tl"
            for ad in adlar:
                for ad in sems:
                    if sems in ad:
                        ad = ad.replace(sems, "")
                if (len(ad) > 0):
                    sembolsuzad.append(ad)
            return sembolsuzad

        fiyatlar = []
        adlar = []
        r = requests.get(links)
        soup = BeautifulSoup(r.content, "html.parser")

        for isimler in soup.find_all("h1", {"class": "seo title"}):
            makale = isimler.text
            yazilar = makale.lower().split()

            for ad in makale:
                adlar.append(ad)
        adlar = yazitemizle(adlar)

        for gruplar in soup.find_all(class_='price-tag'):
            icerik = gruplar.text
            kelimeler = icerik.lower().split()

            for kelime in kelimeler:
                fiyatlar.append(kelime)
        fiyatlar = sembolleritemizle(fiyatlar)

        for kelime in fiyatlar:
            f.write(makale + kelime)
            print(makale + kelime)
    f.close()
def carrefoursa():
    il = giris.get()
    c = ["https://www.carrefoursa.com/kestane-file-500-g-p-30009042",
         "https://www.carrefoursa.com/aptamil-4-cocuk-devam-sutu-1200-g-1-yas--p-30247341"]
    yazi2.config(text="Carrefoursa metin belgesine yazdırıldı.")
    a = il + ".txt"
    f = open(a, "w+")
    yazi.config(text="Dosya adı: %s" % il)
    for links in c:
        def sembolleritemizle(fiyatlar):
            sembolsuzkelime = []
            semboller = "[]''tl"
            for kelime in fiyatlar:
                for sembol in semboller:
                    if sembol in kelime:
                        kelime = kelime.replace(sembol, "")

                if (len(kelime) > 0):
                    sembolsuzkelime.append(kelime)
            return sembolsuzkelime

        def yazitemizle(adlar):
            sembolsuzad = []
            sems = "[]''tl"
            for ad in adlar:
                for ad in sems:
                    if sems in ad:
                        ad = ad.replace(sems, "")
                if (len(ad) > 0):
                    sembolsuzad.append(ad)
            return sembolsuzad

        fiyatlar = []
        adlar = []
        r = requests.get(links)
        soup = BeautifulSoup(r.content, "html.parser")

        for isimler in soup.find_all(class_="name"):
            makale = isimler.text
            yazilar = makale.lower().split()

            for ad in makale:
                adlar.append(ad)
        adlar = yazitemizle(adlar)

        for gruplar in soup.find_all(class_="item-price"):
            icerik = gruplar.text
            kelimeler = icerik.lower().split()

            for kelime in kelimeler:
                fiyatlar.append(kelime)
        fiyatlar = sembolleritemizle(fiyatlar)

        for kelime in fiyatlar:
            f.write(makale + "   " + kelime + "\n")
            print(makale + kelime)
    f.close()
def sokmarket():
    il = giris.get()
    s = ["https://www.sokmarket.com.tr/slim-soft-dis-fircasi-11-p-26169",
         "https://www.sokmarket.com.tr/sakal-tras-makinesi-ss-4075-p-30169/"]
    yazi4.config(text="Şok Market metin belgesine yazdırıldı.")
    a = il + ".txt"
    f = open(a, "w+")
    yazi.config(text="Dosya adı: %s" % il)
    for links in s:
        def sembolleritemizle(fiyatlar):
            sembolsuzkelime = []
            semboller = "[]''tl"
            for kelime in fiyatlar:
                for sembol in semboller:
                    if sembol in kelime:
                        kelime = kelime.replace(sembol, "")

                if (len(kelime) > 0):
                    sembolsuzkelime.append(kelime)
            return sembolsuzkelime

        def yazitemizle(adlar):
            sembolsuzad = []
            sems = "[]''tl"
            for ad in adlar:
                for ad in sems:
                    if sems in ad:
                        ad = ad.replace(sems, "")
                if (len(ad) > 0):
                    sembolsuzad.append(ad)
            return sembolsuzad

        fiyatlar = []
        adlar = []
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(links)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for isimler in soup.find_all("h1", {"class": "info-title"}):
            makale = isimler.text
            yazilar = makale.lower().split()

            for ad in makale:
                adlar.append(ad)
        adlar = yazitemizle(adlar)

        for gruplar in soup.find_all(class_='pricetag info-price'):
            icerik = gruplar.text
            kelimeler = icerik.lower().split()

            for kelime in kelimeler:
                fiyatlar.append(kelime)
        fiyatlar = sembolleritemizle(fiyatlar)
        for kelime in fiyatlar:
            f.write(makale + "  " + kelime + "\n")
            print("\n" + makale + "  " + kelime + "\n")
            driver.close()
    f.close()
    driver.quit()
def karsilastir():
    url = 'https://text-compare.com/'
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open_new(url)


pencere=Tk()
width=759
height=593
screenwidth = pencere.winfo_screenwidth()
screenheight = pencere.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
pencere.geometry(alignstr)
pencere.resizable(width=False, height=False)

#migros market
yazi6=Label(pencere)
yazi6=tk.Label(pencere)
ft = tkFont.Font(family='Times',size=10)
yazi6["font"] = ft
yazi6["fg"] = "#333333"
yazi6["justify"] = "center"
yazi6["text"] = "Migros Market"
yazi6.place(x=60, y=40, width=197, height=30)
yazi6.config(text="Migros  Market")

GButton_67=tk.Button(pencere)
GButton_67["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_67["font"] = ft
GButton_67["fg"] = "#000000"
GButton_67["justify"] = "center"
GButton_67["text"] = "Yazdır"
GButton_67.place(x=30,y=90,width=279,height=83)
GButton_67["command"] = migros

#carrefoursa market
yazi2=Label(pencere)
yazi2=tk.Label(pencere)
ft = tkFont.Font(family='Times',size=10)
yazi2["font"] = ft
yazi2["fg"] = "#333333"
yazi2["justify"] = "center"
yazi2["text"] = "Carrefoursa Market"
yazi2.place(x=70,y=210,width=200,height=32)
yazi2.config(text="Carrefoursa Market")


GButton_550 = tk.Button(pencere)
GButton_550["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_550["font"] = ft
GButton_550["fg"] = "#000000"
GButton_550["justify"] = "center"
GButton_550["text"] = "Yazdır"
GButton_550.place(x=30,y=270,width=279,height=83)
GButton_550["command"] = carrefoursa

#şok market
yazi4=Label(pencere)
yazi4=tk.Label(pencere)
ft = tkFont.Font(family='Times',size=10)
yazi4["font"] = ft
yazi4["fg"] = "#333333"
yazi4["justify"] = "center"
yazi4["text"] = "Şok Market"
yazi4.place(x=70,y=380,width=209,height=30)
yazi4.config(text="Şok Market")

GButton_743=tk.Button(pencere)
GButton_743["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_743["font"] = ft
GButton_743["fg"] = "#000000"
GButton_743["justify"] = "center"
GButton_743["text"] = "Şok Market"
GButton_743.place(x=40,y=440,width=279,height=83)
GButton_743["command"] = sokmarket

#karşılaştır
GButton_262 = tk.Button(pencere)
GButton_262["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=10)
GButton_262["font"] = ft
GButton_262["fg"] = "#000000"
GButton_262["justify"] = "center"
GButton_262["text"] = "Karşılaştır"
GButton_262.place(x=430,y=220,width=290,height=92)
GButton_262["command"] = karsilastir

#yazi
yazi=Label()
yazi.config(text="Dosya adı girilmesi zorunlu.")
yazi.pack()
giris=Entry()
giris.pack()
pencere.mainloop()




