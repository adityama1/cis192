import requests
from bs4 import BeautifulSoup

url = 'http://www.seas.upenn.edu/~adityama/'
r = requests.get(url)
soup = BeautifulSoup(r.content)

#for link in soup.find_all("a"):
 #   #print link.get("href")
  #  if 'http' or 'https' in link:
   #     print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

gdata = soup.find_all("div",{"class":"info"})
print gdata

