import time
from datetime import datetime

# Widows
# C:\Windows\System32\drivers\etc

# Mac and Linux
# /etc/hosts

hosts_temp = "hosts"
host_path = r"/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com",
                "facebook.com", "www.reddit.com", "reddit.com"]


# print(datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8))
# print(datetime.now())
# print(datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16))

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
        print("Working hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")

    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Free time")
    time.sleep(5)
