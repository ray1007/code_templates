import re
import requests

from bs4 import BeautifulSoup()

# this is the example html content.
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# parse it.
soup = BeatifulSoup(html_doc, 'html.parser')
soup = BeatifulSoup(html_doc, 'lxml')

# (dot) attribute name is to access the HTML child nodes
# (square brackets) key name is to access the HTML attributes
soup.body.p['class']


# navigate the tree: 

# .contents .string .children .descendants 

# .parent .parents
# HTML DOM is a tree, so each node has exactly 1 parent. 
# and parents form a single path to root.

# .next_sibling(s) .prev_sibling(s)
# .next_element(s) .prev_element(s)


# Search nodes: find() find_all()
# the filters pass to these functions could be:
# - string
# - regex
# - list, match any of the element
# - bool
# - function taking the element as arguemnt, and returning True/False

# 2 main funciton arguments: `name`, `attrs`. They act like filters.
# `name` corresponds to the tag name, like div, a, button
# `attrs` are the attributes.
soup.find_all(name='div', attrs={'id': 'my-div', 'class': 'short-button'})

# find the node containing that matches some string content:
soup.find(name='a', string='Elsie')
soup.find(name='a', string=re.compile('^El'))

# search with CSS selector: .select()




