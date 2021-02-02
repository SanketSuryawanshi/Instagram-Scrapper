# 1) Fetching The Html with requset module
# 2) Parsing That HTMl With Beautiful Soup & html Parser
# 3) Html Tree Traversal 

import requests
import html5lib
from bs4 import BeautifulSoup

r = requests.get("https://www.instagram.com/sanket_03_12/")

soup = BeautifulSoup(r.content,"html.parser")

data = soup.find_all('meta', attrs={'property':'og:description'})
text = data[0].get('content').split()

print(f"Usernam => {text[-1]}")
print(f"Followers => {text[0]}")
print(f"Following => {text[2]}")