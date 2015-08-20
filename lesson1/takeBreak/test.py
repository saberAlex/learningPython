import webbrowser 
import time


print "Hello world"

for x in range(0,3):
	print "HELLO " + str(x) + " " + time.ctime()
	time.sleep(5)
	webbrowser.open("http://google.com")