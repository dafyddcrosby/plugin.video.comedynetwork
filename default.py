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
    url = "%s/VideoLibraryContents.aspx?GetChildOnly=true&SeasonID=%i" % \
        (AJAX_URL, season_id)
    scrape = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(scrape).findAll('a', id=True)
    episodes = {}
    for alink in soup:
        episode_id = alink["id"].replace("Episode_", "")
        episodes[alink.text] = int(episode_id)
    return episodes

def get_episode_clips(episode_id):
    """
    This is where it gets a bit tricky
    """
    url = "http://esi.ctv.ca/datafeed/content.aspx?cid=%i" % episode_id
    scrape = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulStoneSoup(scrape).find('playlist').findAll('element')
    clips = {}
    for clip in soup:
        clips[clip.title.contents[0].strip()] = int(clip["id"])
    return clips

def main():
    pass
    

main()
