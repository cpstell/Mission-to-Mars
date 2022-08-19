#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# set your executable path in the next cell, then set up the URL (NASA Mars News (Links to an external site.)) for scraping.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.head()


# In[14]:


# New Image setup
# df = pd.read_html('https://galaxyfacts-mars.com')[0]
# df.columns=['description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


# convert DataFrame back into HTML-ready code 
df.to_html()


# ## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1 Use the browser to visit the URL.
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image and titles for each hemisphere.
links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    
    # create an empty dictionary to store img and title for each hemisphere
    hemisphere = {}
    
    # find img and click though to next page
    browser.find_by_css('a.product-item img')[i].click()
    
    # find sample image and extract
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['image_url'] = sample_elem['href']
    
    # get the title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # append list with dictionary
    hemisphere_image_urls.append(hemisphere)
    
    # navigate back to the start page
    browser.back()


# In[18]:


# 4. Print the list that hold the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:





# In[19]:


# end the automated browsing session
browser.quit()


# In[ ]:




