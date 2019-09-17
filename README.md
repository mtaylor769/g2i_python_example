# g2i_python_example

G2i Python coding test.

## Quickstart

```
git clone git@github.com:mtaylor769/g2i_python_example.git g2i
cd g2i
docker build .
docker run -p 8080:5000

curl -L http://localhost:8080
```

or navigate to [http://localhost:8080](http://localhost:8080) in your browser.

benchmark time: {'time': 15.507785081863403}

## Project Scope (instructions from G2i)

Write a program that given a domain, builds a site map. You should spend no more than 2-3 hours on this. Don't worry if the code isn't perfect. The site map should catalog all links and images on a page and visit other pages on the same domain. For example, if we start with www.mozilla.org I expect the site map output to be a json document that is saved
to the filesystem with this structure:

```
[
  {"page_url": "https://www.mozilla.org/en-US/",
  "links": ["https://www.mozilla.org/en-US/about/", "https://play.google.com/store/
  "images": ["https://www.mozilla.org/media/contentcards/img/home-2019/card_1/send.
  },
  {"page_url": "https://www.mozilla.org/en-US/developer/",
  "links": ["https://www.mozilla.org/en-US/about/", "https://play.google.com/store/
  "images": ["https://www.mozilla.org/media/contentcards/img/home-2019/card_1/send.
  },
...
]
```

We expect this code to be correct, detecting cycles and other strange or undefined behaviors and throwing reasonable errors.

Here is some example python code signature but feel free to modify or use any language

```
def build_site_map(starting_url: string, max_depth: int = 10):
  json_site_map = {}
  // YOUR code here
  return json_site_map
```
