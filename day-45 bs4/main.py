from bs4 import BeautifulSoup
import lxml

with open("index.html") as file:
    soup = BeautifulSoup(file.read(), "lxml")
    
print(soup.title.name)