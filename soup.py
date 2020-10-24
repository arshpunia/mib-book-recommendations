from bs4 import BeautifulSoup
import requests

#r = requests.get('https://ritholtz.com/category/podcast/mib/')
##r = requests.get('https://ritholtz.com/2020/06/mib-ron-carson/')
r = requests.get('https://ritholtz.com/2020/06/mib-luke-ellis/#more-248836')
soup = BeautifulSoup(r.text,'html.parser')

"""
for link in (soup.find_all('a')):
    if 'mib' in link.get('href') and 'ritholtz.com' in link.get('href'):
        print(link.get('title'))
"""
"""
for link in soup.find_all('a'):
    if link.get('title') != None:
        if 'mib-' in link.get('href'):
            print(link.get('href')+"\t"+link.get('title')) 
"""

known_list = []
##for link in soup.find_all('a'):
pc_headers = soup.find("div",{"class":"pf-content"})
print(pc_headers.h3.text )

"""
for link in soup.find("h3",text="Luke Ellis Favorite Books").find_all_next('a'):
    if link.get('title') == None and link.get('href').startswith('https://www.amazon.com/'):
        if not link.get('href') in known_list:
            print(link.get('href')) 
            known_list.append(link.get('href'))
            
"""