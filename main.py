from bs4 import BeautifulSoup;

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    #New BeautifulSoup instance
    bs = BeautifulSoup(content, "lxml")

    sections = bs.find_all('div', class_='section')
    
    for section in sections:
        print(section.button.text)

    