import telnetlib
import os
import sys
import time


ip_addr='50.76.53.27'
TELNET_PORT=23
TELNET_TIMEOUT=6
username = "pyclass"
password = "88newclass"

def telnet_connect(ip_addr, TELNET_PORT,TELNET_TIMEOUT):
 try:
  return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
 except socket.error:
  sys.exit('Connection Timed Out')

def login(remote_conn,username,password):
 remote_conn.read_until('sername',TELNET_TIMEOUT)
 remote_conn.write(username + '\n')
 remote_conn.read_until('assword',TELNET_TIMEOUT)
 remote_conn.write(password + '\n')

def send_command(remote_conn,cmd):
 cmd=cmd.rstrip()
 remote_conn.write(cmd + '\n')
 time.sleep(1)
 return remote_conn.read_very_eager()
 

def main():

 ip_addr='50.76.53.27'
 TELNET_PORT=23
 TELNET_TIMEOUT=6
 username = "pyclass"
 password = "88newclass"
 
 remote_conn=telnet_connect(ip_addr,TELNET_PORT,TELNET_TIMEOUT)
 # remote_conn=telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
 #print dir(remote_conn)
 #print type(remote_conn)
 login(remote_conn,username,password)
 #remote_conn.read_until('sername',TELNET_TIMEOUT)
 #remote_conn.write(username + '\n')
 #remote_conn.read_until('assword',TELNET_TIMEOUT)
 #remote_conn.write(password + '\n')
 #time.sleep(1)
 #output=remote_conn.read_very_eager()
 #print output
 
 output=send_command(remote_conn,'show ip int brief')
 #remote_conn.write('show ip int brief' + '\n')
 #time.sleep(1)
 #output=remote_conn.read_very_eager()
 print output
 remote_conn.close()


if __name__ == "__main__":
   main()


