import os, sys

os.chdir("/home/pi/Documents/Python-Beginner-Pi-Projects/TELEGRAM_BOT/")
os.system('find /motion/* -mtime +2 > log_for_deletion.txt')
print 'log_for_deletion has been printed'

f=open("/home/pi/Documents/Python-Beginner-Pi-Projects/TELEGRAM_BOT/log_for_deletion.txt", "r")
lines = f.readlines()
for i in lines:
    os.system('sudo rm %s' % i.rstrip('\n'))
    print('deleting %s' % i.rstrip('\n'))
f.close()
