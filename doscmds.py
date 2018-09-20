import subprocess
import nmap

DOS_CMD = ["ASSOC",'ATTRIB','BREAK','BCDEDIT','CACLS','CD','CHDIR',\
'CHCP','CHKDSK','CHKNTFS','CLS','CMD','color','comp','compact'\
,'convert','copy','date','DEL','DIR','DISKCOMP','DISKCOPY','DISKPART'\
'DOSKEY','DRIVERQUERY','ECHO','set','netsh']

scan = ()
def readdoc(fname):
    with open(fname) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    return content
#System call to system cmd line returns out
def getCMDout(X):
    result = subprocess.check_output(X, shell=True).splitlines()
    data = result[2]
    print(data)
#get ip returns the systems ip information
def getIP():
    getip = 'ipconfig /all'
    result = subprocess.check_output(getip, shell=True).splitlines()
    return result
#set the ip changes the users ip information
#setIP('MAIN ETH','10.10.10.2','255.255.255.0','1.1.1.1')
def setIP(ifacename,ipaddr,subnet,defgateway):
    setip = 'netsh interface ip set address name="{}" static {} {} {}'.format(\
    ifacename,ipaddr,subnet,defgateway)
    result = subprocess.check_output(setip, shell=True).splitlines()
    return result
#getARP returns the arp information of the system
def getARP():
    getarp='arp -a'
    result = subprocess.check_output(getarp, shell=True).splitlines()
    return result
#To ping the network
def pingNet():#ip='192.168.1.1',time='5'):
    pingip='ping 192.168.33.2'
    #pingip='ping {} -n 1 -w {}'.format(ip,time)
    try:
        result=subprocess.check_output(pingip)
        return result
    except subprocess.CalledProcessError as e:
        print(e)
def pinghost():
    try:
        subprocess.check_output("dir /f",shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}):{}".\
        format(e.cmd, e.returncode, e.output))
#nmap sweep
def sweepNet():
    print('--------------------------------')
    # Asynchronous usage of PortScannerAsync
    nma = nmap.PortScanner()
