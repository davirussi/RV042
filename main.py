### simple way to scrap list os ips and macs from RV042 you will need the html with the information.
import re
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def scrapper(file):
    out=[]
    for line in file:
        if re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} =>", line):
            dic={}
            dic['ip']=(re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line).group(0))
            dic['mac']=(re.search("([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})",line).group(0))
            dic['name']=(re.search(" 1 .{1,15}'>",line).group(0)[2:-2])
            out.append(dic)
    return out 


def generater(dic):
    outfile=open('out.txt','w')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.txt')    
    with open('ipmacname.txt', 'w') as f:
        f.write(template.render(data=dic))
    
def fun(filename):
    file=open(filename,'r')
    dic=scrapper(file)
    generater(dic)

def main():
    fun('dhcp_setup.htm')
    
main()
    