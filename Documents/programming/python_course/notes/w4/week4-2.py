#1 week3.1
class IDoNotLikeYou(Exception):
    DEVILS_NUMBER = 666
    #print('This is the devil\'s number')

class notPosInt(Exception):
    paass

class notInt(Exception):
    pass

def getInt(prompt='asda: '):
    try:
        return int(input(prompt))
    except ValueError:
        print()
    except ZeroDivisionError:
        print
    raise notInt() as e:
        print()
        
def getPosint():
    n = getint()
    if n>0:
        return n
    else:
        raise notPosInt() as e:
            print()
    
try:
    x = getPosint()
except notInt() as e:
    print(e.args)
except notPosInt() as e:
    print(e.args)
else:
    print(x)
finally:
    if x==666:
        raise IDoNotLikeYou()
    
    
    



#2
import io

f = open('demo.txt')
try:
    #https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
#    with f.write('fsdgdf') as
    f.write('asd')
except io.UnsupportedOperation:
    print('not writeble')
finally:
    f.close()
    print('closed')
    




### gstreamer aside
#    https://www.raspberrypi.org/forums/viewtopic.php?p=462668#p4626684
#    https://raspberrypi.stackexchange.com/questions/78867/uv4l-audio-video-recording-or-stream
#    https://codefluegel.com/en/howto-livestream-with-raspberry-pi-and-gstreamer/
#    https://www.linux-projects.org/uv4l/tutorials/rtmp-server/
#    https://www.raspberrypi.org/forums/viewtopic.php?t=71206
#    https://www.linux-projects.org/uv4l/tutorials/
##





#3
communication protocol layers:
    link and physical
    internetwork:                                           ip, icmp;                            |            arp (Address Resolution Protocol)
    transport:           tcp                                    |                    udp
    app:telnet ftp smtp http (https uses tls now) x kerberos; dns snmpt; NFS RPC FTTP OTHER      |            mac address
    

IP PACKET MAKEUP: ip datagram ipv6

tcp:
    tcp/ip header fields altered by NATs outgoing packet
    uniqueness of checksum
    python sockets howto
    
python modules for protocols





#4
#modules
#name module "name"
DEVILS_NUMBER = 666
print('loading module mine')

def get():
    print('number is {}'.format(DEVILS_NUMBER))
          
def getInt(prompt = 'asd'):
    return int(input(prompt))

def askForDevilsN():
    s = getInt()
    if s = 666:
        get()
    else:
        print('asda')
          
#new file
from mine import get, askForDevilsN
from mine import DEVILS_NUMBER as NICE_NUMBER

get()
askForDevilsN()
assert mine 


#imports from folder
#os.environ set default
#one folder up solution sys.path(os....)
#package structure
#pyenv
#folder conventions
#all files with small letters (win reads no capital letters)
#https://github.com/kennethreitz/samplemod
#https://docs.python-guide.org/writing/structure/
#__asds__ -> dundr asds

#4.1 import
#package/subpackage/__init__.py
#package/subpackage/mod.py
#from package.subpackage.mod import function
#body
# mod.__name__ may be __init__

#4.2 run as program
#__main__
#__name__ == __main__




#5
#run with name
def Hi(sys.argv):
    print(sys.argv)
    print('Hi', sys.argv[1:])
    
    
    
hw 16/17
