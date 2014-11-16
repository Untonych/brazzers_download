#!/usr/local/bin/python
 
import os
import re
import httplib2
from bs4 import BeautifulSoup
 
 
class Brazzers(object):
 
    def __init__(self):
        self.http = httplib2.Http()
 
    def _get_magnet_link(self, item):
        if 'magnet:' in item['href']:
            return item['href']
 
    def get_scene_titles(self, len=1):
        status, response = self.http.request('http://www.brazzers.com/videos/')
        scene_titles = []
        for item in BeautifulSoup(response).find_all('div', class_='scene-card-title'):
            try:
                title = item.find('a')['title']
            except AttributeError, KeyError:
                pass
            scene_titles.append(title)
        return scene_titles[:len]
 
    def open_magnet_links(self, scene_titles):
        for title in scene_titles:
            status, response = self.http.request('http://fastpiratebay.com/search/%s' % title.replace(' ', '%20'))
            print status.get('content-location')
            for item in BeautifulSoup(response).find_all('a'):
                link = self._get_magnet_link(item)
                if link:
                    os.system('open "%s"' % link)
                    break
 
    def daily(self):
        scene_titles = self.get_scene_titles(2)
        self.open_magnet_links(scene_titles)
 
 
Brazzers().daily()

