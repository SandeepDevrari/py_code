##this is an client socket program impementation in python 3
import socket as s
cs=s.socket(s.AF_INET,s.SOCK_STREAM);
host=s.gethostname();
port=9999;
cs.connect((host,port));
msg=cs.recv(1024);
cs.close();