#imports regex, beautiful soup for web scraping and decimal modules
from re import sub
import bs4
import decimal as Decimal
import matplotlib
import numpy


def main():
    #List that holds the salaries of all of the players
    salaries = []
    #There can be no more than 125 players that you need to account for
    #We can start with the variable 'numPlayers = 125' andtif we cannot parse the data correctly
    #(e.g. there is no data) then we can just subtract the number of players by 1, so it does
    #not interfere with any of the data
    numPlayers = 125
    count = 0

    rg = "^(\d+)"
    with open("questionnaire-148920.appspot.com.html") as fp:
        soup = bs4.BeautifulSoup(fp,"html.parser")


    table = soup.find('table',{'class': 'table'})
    count = 0
    
    numElements = len(soup.find_all('td'))
    for x in numElements:
        text = salaries[x].renderContents()
        trimmed_text = text.strip()
        print (trimmed_text)


    

    

main()
 


    
