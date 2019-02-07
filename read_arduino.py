import time
import serial

file=open("arduino.dat","a")
file.write("\n")

s=serial.Serial('/dev/ttyUSB0',9600)

a1="289AD700805D" 


min0=-1
n1=0
tsum1=0.0

while True:
 t=time.localtime(time.time())
# print time.localtime()[:6]
 #time.struct_time(tm_year=2010, tm_mon=2, tm_mday=7, tm_hour=14, tm_min=46, tm_sec=58, tm_wday=6, tm_yday=38, tm_isdst=0)
 year=t.tm_year
 mon=t.tm_mon
 mday=t.tm_mday
 hour=t.tm_hour
 min=t.tm_min
 sec=t.tm_sec
 if min<>min0:
  t1=-99
  min0=min
  if n1>0:

#     print year,mon,mday,hour,min,t1
     if min0<>-1 and n1>1 and t1<100:
       t1=int(tsum1/n1*100)/100.0
       tsum1=0.0
       n1=0
       fmt="%4d %02d %02d %02d %02d %5.2f" % (year,mon,mday,hour,min,t1)
       print fmt
       file.write(fmt+'\n')
       file.flush()

 data =""
 try:
  data = s.readline()
 except SerialException:
  print "Error reading serial port"
 n1=n1+1 
# print data
 f = float(data)
 tsum1=tsum1+f

