#created with ❤️ in 🇫🇷 by Max21910
import requests
import time

print("created with ❤️ in 🇫🇷 by Max21910")
time.sleep(3)
print("Bereal Status by Max21910")
time.sleep(3)
url = "https://status.bereal.team"

seconds = time.time()
print("Local time:", seconds)
   
response = requests.request("GET", url)
print(response.text)
f= open("BerealStatus.txt","w+")
f.write(response.text)
f.close()
