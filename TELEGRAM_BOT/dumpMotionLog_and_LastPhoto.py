import os, sys

os.chdir('/home/pi/Documents/Python-Beginner-Pi-Projects/TELEGRAM_BOT/')
os.system('find /motion/* -mtime -3 > storico.txt')
print 'storico has been printed'
os.system('tail -n10 storico.txt > log_for_pi.txt')
print 'log_for_pi has been printed'
os.system('tail -n1 storico.txt > photo_to_send.txt')
print 'last photo identified'

f=open("/home/pi/Documents/Python-Beginner-Pi-Projects/TELEGRAM_BOT/photo_to_send.txt", "r")
lines = f.readlines()
lines[0].rstrip('\n')
print str(lines[0].rstrip('\n'))
os.system('cp %s /home/pi/Documents/Python-Beginner-Pi-Projects/TELEGRAM_BOT/sospetto.jpeg' % lines[0].rstrip('\n'))
f.close()
