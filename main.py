### simple way to scrap list os ips and macs from RV042 you will need the html with the information.
import re

def scrapper(file):
    out={}
    ip=[]
    mac=[]
    name=[]
    for line in file:
        if re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} =>", line):
            ip.append(re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line).group(0))
            mac.append(re.search("([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})",line).group(0))
            name.append(re.search("1 .{1,15}'>",line).group(0)[2:-2])
    out['ip']=ip
    out['mac']=mac
    out['name']=name
    return out 
    
def fun(filename):
    file=open(filename,'r')
    list=scrapper(file)

def main():
    fun('dhcp_setup.htm')
    
main()
    