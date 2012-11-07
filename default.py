#import xbmc
#import xbmcgui
#import xbmc
import urllib
import BeautifulSoup

AJAX_URL = "http://watch.thecomedynetwork.ca/AJAX/"

def list_shows():
    url = "%s/VideoLibraryContents.aspx" % AJAX_URL
    scrape = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(scrape).findAll('a')
    shows = {}
    for alink in soup:
        shows[alink.text] = int(alink["id"])
    return shows

def list_seasons(show_id):
    url = "%s/VideoLibraryContents.aspx?GetChildOnly=true&ShowID=%i" % \
        (AJAX_URL, show_id)
    scrape = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(scrape).findAll('a')
    seasons = {}
    for alink in soup:
        seasons[alink.text] = int(alink["id"])
    return seasons

def list_episodes(season_id):
    """
    TODO - figure out how we list the episodes
    """
    url = "%s/VideoLibraryContents.aspx?GetChildOnly=true&SeasonID=%i" % \
        (AJAX_URL, season_id)
    scrape = urllib.urlopen(url)
    return scrape



def main():
    pass
    

main()
