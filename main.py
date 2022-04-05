from bs4 import BeautifulSoup;
import requests

# Example to find html elements
# with open('index.html', 'r') as html_file:
#     content = html_file.read()
    
#     #New BeautifulSoup instance
#     bs = BeautifulSoup(content, "lxml")

#     sections = bs.find_all('div', class_='section')
    
#     for section in sections:
#         print(section.button.text)

#Scraping a real website
html_page = requests.get('https://echo.uib.no/event').text
soup = BeautifulSoup(html_page, 'lxml')

eventsDiv = soup.find('div', class_='css-jy27e')
events = eventsDiv.find_all('p')
linksToEvents = eventsDiv.find_all('a')

i = 0
link = 0
while (i < len(events) - 1):
    print(events[i].text, events[i+1].text,"https://echo.uib.no"+str(linksToEvents[link]['href']))
    i+=2
    link+=1

    