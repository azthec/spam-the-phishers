import random
import requests
import linecache
import time

# curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'email=asd%40as.asdasd&password=asd&passw=asd' http://correoelectronico.eu3.org/confirmation.php

SUCCESS_COUNTER = 0
PROXIES = [('http', "http://213.58.202.70:54214"),
           ('http', "http://79.168.179.50:8080"),
           ('http', "http://194.38.137.252:3128"),
           ('socks4', "socks4://62.28.230.50:39698"),
           ('socks4', "socks4://5.158.46.93:4145"),
           ('socks4', "socks4://37.189.106.245:58498"),
           ('socks4', "socks4://2.80.105.119:37329"),
           ('socks4', "socks4://85.138.136.189:4145"),
           ('socks4', "socks4://185.51.92.108:51327"),
           ('socks4', "socks4://213.58.202.70:31431"),
           ('socks4', "socks4://188.81.125.155:4145"),
           ('socks4', "socks4://109.51.16.186:4145")]


def random_line(filename, lines):
    return linecache.getline(filename, random.randint(0, lines))


def send_fake():
    global SUCCESS_COUNTER
    URL = 'http://correoelectronico.eu3.org/confirmation.php'
    SUCCESS_CONTENT = """<center><br><br><h3>Thank You!<br>Your e-mail account will be verify in the next 48hours.</h3><br><br>PLEASE DO NOT RESEND!<br><br><b>WARNING:</b> THIS MESSAGE IS FROM THE SYSTEM ADMINISTRATOR!"""
    domain = random_line("domains.txt", 3620).rstrip()
    password = random_line("top1000000.txt", 999999).rstrip()
    faculty_mail = bool(random.getrandbits(1))
    if faculty_mail:
        user = "up20" + str(random.randint(0, 18)).rjust(2, "0")
        user = user + str(random.randint(0, 99999)).rjust(5, "0")
        domain = "fc.up.pt"
    else:
        user = random_line("top1000000.txt", 999999)
    email = user.rstrip() + "@" + domain.rstrip()
    session = requests.session()

    proxy = random.choice(PROXIES)
    r = requests.post(URL,
                      data={'email': email,
                            'password': password,
                            'passw': password},
                      proxies={proxy[0]: proxy[1]},
                      allow_redirects=True)
    if str(r.content, "utf8") == SUCCESS_CONTENT:
        SUCCESS_COUNTER += 1
    print("{0: <30} | {1: <20} | {2: <5} | {3},".format(email, password, SUCCESS_COUNTER, proxy))


def main():
    print("{0: <30} | {1: <20} | {2: <5} | {3}".format("email", "password", "ctr", "proxy"))
    while(True):
        try:
            send_fake()
            time.sleep(random.randint(5,10))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()