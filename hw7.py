''' Homework 7
-- Due Monday, October 24th at 23:59
-- Before starting, read
https://www.cis.upenn.edu/~cis192/homework/
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
'''

import requests
from bs4 import BeautifulSoup

def music_recs(artist):

    ''' Search ifyoudig.net for the specified artist. Do some searches yourself
    to see how this works. You only have to support artists that appear here:
    http://ifyoudig.net/autocomplete.php. 
    If any other input is given, throw an exception with the message:
    "Artist not found.".

    You should convert the artist name to the specified hyphenated slug, and then
    query the appropriate url. Return a list of the top 10 recommended artists.

    Note that most of the artist names are links, but some aren't;
    e.g. see http://ifyoudig.net/laura-marling. You should be able to handle
    either case.

    Assume that the artist will have correct capitalization if a valid artist.
    '''
    main_url='http://ifyoudig.net/'
    url = 'http://ifyoudig.net/autocomplete.php'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    #print r.text
    tag = soup.strings
    for line in tag:
        if line.find(artist) != -1:
            print "found"
            a = 1
        else:
            print "not found"
    if a:
        newUrl = main_url + artist
        r1 = requests.get(main_url)
        print newUrl
    #for line in soup:
     #   print type(line)
        #if artist in line:
      #  print type(line.text) #all the actual text for each line



def xkcd(comic_num):
    ''' Pull up the comic_num-th xkcd comic on http://xkcd.com/
        For example: comic_num = 1488 --> http://xkcd.com/1488/
    Return a dictionary with the keys:
        'image_path', 'comic_title', and 'title_text'
    The values should be:
        'image_path' -> a relative file path to a downloaded image of the comic
                    Store the file in a directory called imgs, and do not
                    assume that directory already exists. The os module may be
                    helpful here.
        'comic_title' -> The string that is the title of the comic
        'title_text' -> The string that is the title attribute of the image
    If comic_num is beyond the range of valid comics at the time of the query,
    raise a ValueError with the message:
        '[comic_num] is an invalid xkcd comic.'
    You should raise this error only if the request results in
    a "Not Found" status code (see `requests.codes.not_found`).
    '''
    pass


def main():
    music_recs('eminem')


if __name__ == "__main__":
    main()
