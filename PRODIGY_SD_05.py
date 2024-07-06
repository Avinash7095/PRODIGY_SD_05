import requests
from bs4 import BeautifulSoup
import pandas as pd

books=[]
for i in range(1,5):
  url=f"https://books.toscrape.com/catalogue/page-{i}.html" # Use f-string for formatting
  response=requests.get(url)
  response.raise_for_status() # Check for HTTP errors
  soup=BeautifulSoup(response.content,"html.parser")
  ol=soup.find('ol') 
  if ol is None:
    print(f"Warning: Could not find 'ol' tag on page {i}. Skipping...")
    continue # Skip to the next page if 'ol' is not found
  articles =ol.find_all('article',class_='product_pod')

  for article in articles:
      image=article.find('img')
      title=image.attrs['alt']
      star=article.find('p')
      star=star['class'][1]
      price=article.find('p',class_='price_color').text
      price=float(price[1:])
      books.append([title,price,star]) # Append 'star' instead of 'str'import requests
df=pd.DataFrame(books,columns=['title','price','star Rating'])
df.to_csv('books.csv')