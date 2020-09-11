from threading import Thread
import subprocess
from queue import Queue

queue5 = Queue()

iplist = []
for ipip in range(256):
    ip = '192.168.13.' + str(ipip)
    iplist.append(ip)

def pinger(i, q):
    while True:
        ip = q.get()
        print("Thread %s : Pinging: %s "% (i, ip))
        ret = subprocess.call('ping -c 1 %s' %ip,
                              shell = True,
                              stdout = open('NUL', 'w'),
                              stderr = subprocess.STDOUT)
        if ret == 0:
            print('%s : is alive' %ip)
        else:
            print('%s : did not respond' %ip)
        q.task_done()

for i in range(3):
    th = Thread(target = pinger, args = (i, queue5))
    th.setDaemon(True)
    th.start()
    
for ip in iplist:
    queue5.put(ip)
    
print("Main Thread waiting...")
queue5.join()
print('Done')
