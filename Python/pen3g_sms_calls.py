#!/usr/bin/python

#Envio de sms e tokes para telefones via pen 3G
#Vasco Santos
#V0.1 17/06/2013


import serial
import time

class TextMessage:
    def __init__(self, recipient="123456789", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

class VoiceCall:
    def __init__(self, dialledNumber='000000'):
        self.dialledNumber = dialledNumber

    def dialNumber(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
        self.ser.write('ATZ\r')
        #print "->"+self.ser.read(5)
        ## ATZ : Restore profile ##
        #time.sleep(0.3)
        #self.ser.write('ATI \r')

        #time.sleep(0.5)
        #print "Info:"+self.ser.read(150)
        #self.ser.write('AT+COPS=0,0\r')
        #print "Operator:"+self.ser.read(50)

        #time.sleep(0.5)
        #self.ser.write('AT+CSQ\r')
        #print "Signal:"+self.ser.read(50)

        time.sleep(0.3)
        self.ser.write('AT+CLIR=2\r')
        #print "->"+self.ser.read(50)

        #time.sleep(0.5)
        #self.ser.write('ATD*#123#\r')
        #print "->"+self.ser.read(50)

        time.sleep(0.3)
        self.ser.write('ATD' + self.dialledNumber + ';\r')
        print "->"+self.ser.read(50)
                ## ATD : Dial command ##
                ## semicolon : voice call ##
        time.sleep(0.5)
        self.ser.write(chr(26))
        time.sleep(1)

    def endCall(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CHUP\r')
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

#envio sms
#sms = TextMessage("035191XXXXXXX","This is the message to send.")
#sms.connectPhone()
#sms.sendMessage()
#sms.disconnectPhone()

#chamada
callPhone = VoiceCall("035191XXXXXXX")
callPhone.dialNumber()
time.sleep(15)
callPhone.endCall()
callPhone.disconnectPhone()
 