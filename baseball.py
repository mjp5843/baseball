#imports regex, beautiful soup for web scraping and decimal modules

import bs4
#import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from re import sub
from decimal import Decimal
import urllib.request


def main():
    #List that holds the salaries of all of the players
    salaries = []
    valid_salaries = []

    url = 'https://questionnaire-148920.appspot.com/swe/'
    page = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(page,"html.parser")


    table = soup.find('table',{'class': 'table'})

    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        #tds[0] holds the name of the players
        #tds[1] holds the salaries of the players
       
        salaries.append(tds[1].text)
        

    for x in salaries:
        try:
            value = Decimal(sub(r'[^\d.]', '', x))
            valid_salaries.append(value)
        except Exception as e:
            pass

    #Sort that is from High to Low
    valid_salaries.sort(reverse=True)


    valid_salaries = valid_salaries[:125]
    print ('The average is: $',np.mean(valid_salaries))

    #need to convert the Decimals into ints
    int_salaries = [int(x) for x in valid_salaries]

    #creates the box & whisker figure
    fig = plt.figure(1, figsize=(9,6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(int_salaries)

    plt.show()
    fig.savefig('fig1.png', bbox_inches='tight')
    
main()
