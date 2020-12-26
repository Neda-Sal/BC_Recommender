'''
Pull information from drugs.com
'''

from bs4 import BeautifulSoup


def get_titles(soup):
    '''
    input: BeautifulSoup(page.text, 'lxml')
    returns: list of  drug titles
    '''
    return [element.text.strip() for element in soup.find_all(class_ = 'condition-table__drug-name__link ddc-text-wordbreak')]


def get_title_links(soup):
    '''
    input: BeautifulSoup(page.text, 'lxml')
    returns: list of links to the drug info page
    '''
    return ['drugs.com' + elt['href'] for elt in soup.find_all(class_ = 'condition-table__drug-name__link ddc-text-wordbreak')]


def get_avg_ratings(soup):
    '''
    input: BeautifulSoup(page.text, 'lxml')
    returns: list of average ratings as floats 
    '''
    temp = [rating.text.strip() for rating in soup.find_all(class_ = "ddc-text-nowrap")][:-1]
    return [float(rate) for rate in temp]


def get_num_reviews(soup):
    '''
    input: BeautifulSoup(page.text, 'lxml')
    returns: list of number of reviews ints
    '''
    #some have no ratings, so replace those with 0
    temp = []
    for num_ratings in soup.find_all(class_ = "condition-table__reviews ddc-valign-middle"):
        try:
            temp.append(int(num_ratings.text.strip()[:-8]))

        except:
            temp.append(0)
    return temp


def get_review_links(soup):
    '''
    input: BeautifulSoup(page.text, 'lxml')
    returns: list of review links
    '''
    temp = []
    for num_ratings in soup.find_all(class_ = "condition-table__reviews ddc-valign-middle"):
        for link in num_ratings.find_all('a'):
            temp.append('drugs.com' + link['href'])
    return temp

