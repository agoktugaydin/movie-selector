from bs4 import BeautifulSoup
import random
import requests

URL = 'http://www.imdb.com/chart/top'

def main():
    print('IMDB Top 250 ')
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    movietags = soup.select('td.titleColumn')
    innerMovietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    def getYear(movieTag):
        moviesplit = movieTag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [getYear(tag) for tag in movietags]
    actorsList =[tag['title'] for tag in innerMovietags] # access attribute 'title'
    titles = [tag.text for tag in innerMovietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'

    nMovies = len(titles)

    while(True):
        idx = random.randrange(0, nMovies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actorsList[idx]}')

        userInput = input('Do you want another suggestion? (y/[n])? ')
        if userInput != 'y':
            break
    

if __name__ == '__main__':
    main()