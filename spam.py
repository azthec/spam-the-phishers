import random
import requests
import linecache
import time

# curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'email=asd%40as.asdasd&password=asd&passw=asd' http://correoelectronico.eu3.org/confirmation.php

SUCCESS_COUNTER = 0


def random_line(filename, lines):
    return linecache.getline(filename, random.randint(0, lines))


def send_fake():
    global SUCCESS_COUNTER
    URL = 'http://correoelectronico.eu3.org/confirmation.php'
    SUCCESS_CONTENT = """<center><br><br><h3>Thank You!<br>Your e-mail account will be verify in the next 48hours.</h3><br><br>PLEASE DO NOT RESEND!<br><br><b>WARNING:</b> THIS MESSAGE IS FROM THE SYSTEM ADMINISTRATOR!"""

    domain = random_line("domains.txt", 3620).rstrip()
    password = random_line("rockyou.txt", 14344357).rstrip()
    faculty_mail = bool(random.getrandbits(1))
    if faculty_mail:
        user = "up20" + str(random.randint(0, 18)).rjust(2, "0")
        user = user + str(random.randint(0, 99999)).rjust(5, "0")
        domain = "fc.up.pt"
    else:
        user = random_line("rockyou.txt", 14344357)

    email = user.rstrip() + "@" + domain.rstrip()
    session = requests.session()
    r = requests.post(URL,
                      data={'email': email,
                            'password': password,
                            'passw': password},
                      allow_redirects=True)

    if str(r.content, "utf8") == SUCCESS_CONTENT:
        SUCCESS_COUNTER += 1
    print("{0: <30} | {1: <20} | {2}".format(email, password, SUCCESS_COUNTER))


def main():
    print("{0: <30} | {1: <20} | {2}".format("email", "password", "success counter"))
    try:
        while(True):
            send_fake()
            time.sleep(random.randint(120, 900))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
