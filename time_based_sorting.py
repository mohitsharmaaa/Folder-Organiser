import time
import threading

def delay(seconds):
	time.sleep(seconds)
	print(seconds)

a=[10,1,3,4,6]

for number in a:
	thread=threading.Thread(target=delay,args=(number,))	
	thread.start()
