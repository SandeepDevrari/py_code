##this is an server socket program impementation in python 3
import socket as s
ss=s.socket(s.AF_INET,s.SOCK_STREAM);
host=s.gethostname();
port=9999;
ss.bind((host,port));
ss.listen(6);
while True:
    cs,addr=ss.accept();
    print("client address-%s"%str(addr));
    msg='hell'+"\r\n";
    cs.send(msg.encode('ascii'));
    print(msg);
    cs.close();