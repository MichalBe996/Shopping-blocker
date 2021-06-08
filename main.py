
import time
from datetime import datetime
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
stronki = ["www.zara.com", "https://www.zalando.pl/mezczyzni-home/", "https://www.zalando.pl/kobiety-home/"]

while True:
   if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9) < datetime.now() < datetime(datetime.now().year,datetime.now().month,datetime.now().day,18):
    print("Brak dostępu!")
   with open(hosts_path,'r+') as file:
      content = file.read()
      for strona in stronki:
         if strona in content:
            pass
         else:
            file.write(redirect+" "+strona+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
        for line in content:
             if not any(strona in line for strona in stronki):
                file.write(line)
             file.truncate()
print ("Dozwolono!")
time.sleep(5)