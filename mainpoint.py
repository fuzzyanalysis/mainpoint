UNUSED_ARTICLES_FILE = "unused_articles.txt"
RESERVED_TAGS_FILE = "reserved_tags.txt"
DICTIONARY_FILE = "mwords/354984si.ngl"


from bs4 import BeautifulSoup, NavigableString
import urllib
import re
from collections import Counter
import unicodedata
from sys import *

def main():

    f = open(RESERVED_TAGS_FILE, 'r')
    reserved_tags = [line.rstrip('\n') for line in f]
    f.close()


    f = open(UNUSED_ARTICLES_FILE, 'r')
    unused_articles = [line.rstrip('\n') for line in f]
    f.close()

    #f=open('mwords/354984si.ngl', 'r')
    #dictionary = [line.rstrip('\n') for line in f]
    #f.close()


    # Get the URL and markup
    url = "http://www.datasciencebox.com/drupal" #raw_input("which url would you like to scrape?: ")
    doc = urllib.urlopen(url)
    soup = BeautifulSoup(doc)

    #strippedDoc = ''.join(soup.findAll(text=True))
    #strippedDoc = strip_tags(strippedDoc)

    siteWords = []

    for text in soup.findAll(text=True):
        text = strip_tags(text)
        splitText = text.split()
        for splitWord in splitText:
            if splitWord not in reserved_tags and splitWord not in unused_articles:
                #print splitWord
                siteWords.append(splitWord)

    cnt = Counter()
    for word in siteWords:
        cnt[word] += 1

    l = cnt.items()
    l.sort(key = lambda item: item[1], reverse=True)


    for item in l:
        try:
            print repr(item[0])
        except:
            pass


def strip_tags(string):
    return re.sub(r'<.*?>', '', string)

if __name__ == "__main__": main()