#!/usr/bin/env python
import time
import serial
import re

ser = serial.Serial(
 port='/dev/ttyAMA0', baudrate = 9600, timeout=1
)

def read_params():
	ret = ser.write('read')
	if ret>0:
		f = ser.readline()
		d = ser.readline()

		m = re.search('F((\d|\.)+)',f)
		if m:
			fn=m.group(1)

		m = re.search('D(\d+)',d)
		if m:
			dn=m.group(1)

		return (fn,dn)
	return False

		

def set_params(f):
	ret=ser.write(f)
	if ret>0:
		result=ser.readline()
		print(result)
		if 'DOWN' in result:
			return True
	return False	

def set_frequency():
	return set_params( 'F100' )

def set_dutycycle():
	return set_params( 'D037' )




