#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDdUOGutOhweA_X4qU5jhsAQvBMfMVmxAA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query="google"):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=10
  ).execute()

  urls = []
  image_urls = []
  titles = []
  descriptions = []
  data = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      url = "www.youtube.com/embed/" + search_result["id"]["videoId"] + "?autoplay=1&fs=1&autohide=1&controls=0&rel=0"
      image_url = search_result["snippet"]["thumbnails"]["high"]["url"]

      desc = search_result["snippet"]["description"]
      title = search_result["snippet"]["title"]

      print image_url

      url = url.encode("ascii", errors="ignore")
      image_url = image_url.encode("ascii", errors="ignore")
      title = title.encode("ascii", errors="ignore")
      desc = desc.encode("ascii", errors="ignore")

      data.append((url, image_url,title ,desc))
      """
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
      search_result["id"]["videoId"]))
      elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
      search_result["id"]["channelId"]))
      elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
      search_result["id"]["playlistId"]))
      """
    #print "Videos:\n", "\n".join(videos), "\n"
    #print "Channels:\n", "\n".join(channels), "\n"
    #print "Playlists:\n", "\n".join(playlists), "\n"

  return data

if __name__ == "__main__":
  data = youtube_search()
  print len(data)
