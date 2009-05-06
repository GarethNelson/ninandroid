# silly hack, i can't be bothered debugging my broken django templates

import BeautifulSoup
from google.appengine.api import urlfetch

nin_soup = BeautifulSoup.BeautifulSoup(urlfetch.fetch('http://www.nin.com').content) # delicious NIN soup
nin_soup.findAll(id='photo-discussion-link')[0].extract()
nin_soup.findAll(href='http://feeds.nin.com/ninphotoblog')[0].extract()
nin_soup.findAll(id='news-discuss-link')[0].extract()
nin_soup.findAll(attrs={'class':'clear_both'})[0].extract()

photoblog_tree = nin_soup.findAll(id='photo-blog-container')
photoblog = str(photoblog_tree[0])

news_tree = nin_soup.findAll(id='news-container') 
for img in news_tree[0].findAll('img'):
    img.extract()
news = str(news_tree[0])

homepage = """
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<link rel="stylesheet" type="text/css" href="/static/default.css" />

</head>
<body style="background-color:#000000;color:#A00000;">
<table style="border:none;">
<tr><td valign="center" style="text-align:center;">
<img style="margin-left:auto;margin-right:auto;" src="/static/nin_logo.png" alt="NIN"/>
</td></tr>

<tr>
<th style="width:30%%">Photo blog</th>
<th style="width:70%%">News</th>
</tr>

<tr>
<td>%s</td>
<td>%s</td>
</tr>

</table>
</body>
</html>

"""
