import requests
import re
from urllib.parse import urlparse
from parsel import Selector
import json
from pprint import pprint
import time
start = time.time()

def get_all_links(page):
  selector = Selector(page)
  links = set(selector.xpath('//a/@href').getall())
  images = set(selector.xpath('//img/@src').getall())
  return {"links": links, "images": images}

def get_page(page):
  txt = ''
  try:
    response = requests.get(page)
    txt = response.text
  except (requests.exceptions.MissingSchema):
    pass
  return txt

def filter_links(links, domain, roothost):
    newlinks = []
    sublinks = links['links']
    for link in sublinks:
      parsed = urlparse(link)
      if re.search(domain, parsed.netloc) or not parsed.netloc:
        if not parsed.netloc:
          newlinks.append(roothost  + link)
        else:
          newlinks.append(link)
    return newlinks

def build_site_map(starting_url, max_depth = 3):
  # pprint('here');
  # Expected output
  # ##
  # [
  #   {"page_url": "https://www.mozilla.org/en-US/",
  #     "links": ["https://www.mozilla.org/en-US/about/", "https://play.google.com/store/
  #     "images": ["https://www.mozilla.org/media/contentcards/img/home-2019/card_1/send.
  #   },
  #   {"page_url": "https://www.mozilla.org/en-US/developer/",
  #     "links": ["https://www.mozilla.org/en-US/about/", "https://play.google.com/store/
  #     "images": ["https://www.mozilla.org/media/contentcards/img/home-2019/card_1/send.
  #   },
  # ]
  json_site_map = {}

  # YOUR code here
  tocrawl = [starting_url]
  crawled = []
  next_depth = []
  depth = 0

  startUrl = urlparse(starting_url)
  domain = ".".join(startUrl.netloc.split(".")[1:])
  roothost = startUrl.scheme + "://" + startUrl.netloc
  maps = []
  while tocrawl and depth <= max_depth:
      page = tocrawl.pop()
      if page not in crawled:
          links = get_all_links(get_page(page))
          if links['links']:
            nl = filter_links(links, domain, roothost)
          next_depth = nl
          # json_site_map.items(links)
          ls = links['links']
          ims = links['images']
          maps.append( { "page" : page, "links": [ls], "images": [ims]})
          crawled.append(page)
      if not tocrawl:
          tocrawl, next_depth = next_depth, []
          depth = depth + 1
  json_site_map = maps
  end = time.time()
  # append the total running time to the return object
  pprint({'time': (end-start)})
  return json_site_map
