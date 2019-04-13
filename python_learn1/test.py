import time
import eventlet
eventlet.monkey_patch()
with eventlet.Timeout(3,False):
    time.sleep(4)
    print(1)
name= ["四川",]


