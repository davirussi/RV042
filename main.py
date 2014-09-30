### Simple way to scrap list os ips and macs from RV042 firmware  1.3.12.19-tm.
### You will need the html with the information.
import re
from jinja2 import Template, Environment, FileSystemLoader

#return a vector with dicionarys which contains ip, mac, hostname
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

#function to create the file using Jinja2 templates
def generater(dic):
    outfile=open('out.txt','w')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.txt')    
    with open('ipmacname.txt', 'w') as f:
        f.write(template.render(data=dic))

def main():
    filename='dhcp_setup.htm'
    file=open(filename,'r')
    dic=scrapper(file)
    generater(dic)
    
main()