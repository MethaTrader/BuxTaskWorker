import requests as request
from bs4 import BeautifulSoup
import json

# cookie session of seofast
cookies = {"entrance": "", "PHPSESSID": "",
           "taskuser": "tangens"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'From': 'michael@domain.com'  # This is another valid field
}


# save content to file
def save(name, content):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(str(content))


# find tasks selected user
url = 'https://seo-fast.ru/work_tasks?taskuser=tangens'
response = request.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table', attrs={'id': 'load_page_all'}) #find table by id
save("table.html", table.prettify()) #save page table with formatting

#open table
with open('table.html', 'r', encoding='utf-8') as f:
    contents = f.read()
    soup2 = BeautifulSoup(contents, 'lxml')

data = [] #our result
i = 0
for tr in soup2.find_all('tr'): #find all table rows
    price = tr.find("div", {"class": "price_pay"}) #find price
    title = tr.find("div", attrs={'style': 'color: #4e5665;'}) #find title by color style :)
    if title is not None and price is not None: #if element found
        data.append([title.text.strip(), price.text.strip()]) #add to 2d array
    i = i + 1

jsonString = json.dumps(data, ensure_ascii=False) # array to json
save("tasks.json", jsonString) #save to file
