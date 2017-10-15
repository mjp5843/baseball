#imports regex, beautiful soup for web scraping and decimal modules

import bs4
import matplotlib
import numpy
from re import sub
from decimal import Decimal


def main():
    #List that holds the salaries of all of the players
    salaries = []
    valid_salaries = []
    #There can be no more than 125 players that you need to account for
    #We can start with the variable 'numPlayers = 125' andtif we cannot parse the data correctly
    #(e.g. there is no data) then we can just subtract the number of players by 1, so it does
    #not interfere with any of the data
    with open("questionnaire-148920.appspot.com.html") as fp:
        soup = bs4.BeautifulSoup(fp,"html.parser")


    table = soup.find('table',{'class': 'table'})
    count = 0

    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        count = count + 1
        #tds[0] holds the name of the players
        #tds[1] holds the salaries of the players
        print tds[0].text, tds[1].text
        salaries.append(tds[1].text)
        if(tds[1].text == "no salary data"):
            print "First probelm at player:", tds[1].text
        print 'The length of the list is:', len(salaries)


    for x in salaries:
        try:
            value = Decimal(sub(r'[^\d.]', '', x))
            valid_salaries.append(value)
            print value
        except Exception as e:
            pass

    #Sort that is from High to Low
    valid_salaries.sort(reverse=True)
    print '-------------------------------------------'
    print len(valid_salaries)
    for t in valid_salaries:
        print t


    valid_salaries = valid_salaries[:125]
    print 'The average is: ',numpy.mean(valid_salaries)



main()
