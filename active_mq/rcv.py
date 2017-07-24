#!/usr/bin/env python
import stomp
import calendar
import time
import sys

NUM_MESSAGES=10

msgId=0
times = []
f = open('receive.log', 'w')

class SampleListener(object):
    def on_message(self, headers, message):
        print(message)
        global msgId
        global times
        global f
        
        times.append([msgId,calendar.timegm(time.gmtime())])
        msgId+=1
        
        #stopping conditions
        if msgId==NUM_MESSAGES:
        
            print('Received ' + str(len(times)) + ' messages')
            
            for item in times:
                
                msgId = item[0]
                receiveTime = item[1]
                f.write(str(msgId))
                f.write(" ")
                f.write(str(receiveTime))
                f.write("\n")
            print("Done consuming.")
            sys.exit()
            
conn = stomp.Connection10()
 
conn.set_listener('SampleListener', SampleListener())
 
conn.start()
 
conn.connect()
 
conn.subscribe('SampleQueue')

print(' [*] Waiting for messages. To exit press CTRL+C')

conn.disconnect(receipt=None)