from bs4 import BeautifulSoup
import requests
with open ("./index.html","r")as f:
    doc = BeautifulSoup(f,"html.parser")
    print (doc.h1.string.strip())
editDoc = doc.h1.string
editDoc = "Ahmed"
print(editDoc)