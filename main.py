from bs4 import BeautifulSoup;

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    #New BeautifulSoup instance
    bs = BeautifulSoup(content, "lxml")

    h1tags = bs.findAll('h1')
    print(h1tags)
    