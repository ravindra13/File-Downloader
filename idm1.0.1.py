
def handle_client(client_socket,file,s):
    f=open(file,'rb')
    r=f.read(1024)
    client_socket.send(r)
    j=1
    while(r):
        #client_socket.send(r)
        #j=j+1
        r=f.read(1024)
        client_socket.send(r)
        j=j+1
    print 'done sending'
    print j
    print 'packets'
    client_socket.close()
    f.close()
    s.close()


def handle_server(file,noc):
    file=file+str(noc)+".mkv"
    f=open(file,'wb')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    r=s.recv(1024)
    f.write(r)
    k=1
    while(r):
        r=s.recv(1024)
        k=k+1
        f.write(r)
    print 'done receving'
    print k
    print 'packets'
    f.close()
    s.close()






host='0.0.0.0'
port=13131
import socket
import threading
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "for sending file press s \nfor receving file c"
input=raw_input()
if input=='s':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "give file_name"
    file=raw_input()
    #f=open(file,'rb')
    s.bind((host,port))
    s.listen(8)
    client,addr=s.accept()
    print "got connection from ",addr
    client_handler=threading.Thread(target=handle_client,args=(client,file,s))
    client_handler.start()
        #r=f.read(1024)
        #while (r):
            #client.send(r)
            #i=i+1
            #print "sending\n"
            #r=f.read(1024)
        #print 'done sending '
        #print i
        #print ' packets'
        #break
elif input=='c':
    print "give file_name to save into"
    file=raw_input()
    f=open(file,'wb')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "give server's ip address"
    host=raw_input()    
    s.connect((host,port))
    r=s.recv(1024)
    f.write(r)
    i=1
    while (r):
        r=s.recv(1024)
        #print "receving\n"
        f.write(r)
        i=i+1
    print 'done receving '
    print i
    print ' packets'
    f.close()
    s.close()


