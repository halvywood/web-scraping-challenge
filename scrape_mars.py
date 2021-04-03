from splinter import Browser
from bs4 import BeautifulSoup as soup 
import pandas as pd 
import requests 
import time


def scrape():

    ###########################################################################################
    # NASA Mars News
    ###########################################################################################
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = soup(html, 'html.parser')
    title_results = soup.find('div', class_='content_title')
    p_results = soup.find('div', class_='article_teaser_body')
    news_title = title_results[0].text
    news_p = p_results[0].text
    browser.quit()

    print("---------------NASA Mars News Scraping Complete!---------------")

    ##########################################################################################
    # JPL Mars Featured Image
    ##########################################################################################

    executable_path = {'executable_path': ChromeDriverManager().install()}
    featured_image_url = 'https://spaceimages-mars.com/'
    browser.visit(featured_image_url)
    browser.links.find_by_partial_text('FULL IMAGE')
    current_html = browser.html
    image_soup = soup(current_html, 'html.parser')
    partial_img_url = image_soup.find('img', class_='headerimage fade-in')["src"]
    featured_image_url = "https://spaceimages-mars.com/" + partial_img_url
    browser.quit()

    print("---------------JPL Mars Space Images Scraping Complete!---------------")

    ###########################################################################################
    # Mars Facts
    ###########################################################################################

    mars_facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mars_facts_url)

    print("---------------Mars Facts Scraping Complete!---------------")

    ###########################################################################################
    # Mars Hemispheres
    ###########################################################################################
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres_url)
    hemisphere_html = browser.html

    hemisphere_soup = soup(html_hemispheres, 'html.parser')
    hemisphere_img_class = hemisphere_soup.find_all('div', class_='item')   
    

    main_url = "https://marshemispheres.com/"
    hemisphere_image_urls = []

    for i in hemisphere_img_class:
        img_title = i.find('h3').text
        partial_img_url = i.find('a')['href']

    
        browser.visit(main_url+partial_img_url)

    
        img_html = browser.html
    
    
        img_soup = soup(img_html, 'html.parser')
    
    
        individual_img_partial_url = img_soup.find('img', class_='wide-image')['src']
    
    
        individual_img_url = main_url + individual_img_partial_url

    
        hemisphere_image_urls.append({"title" : img_title, "img_url" : individual_img_url})
 
    browser.quit()

    print("---------------Mars Hemispheres Scraping Complete!---------------")

    ###########################################################################################
    # Store the return value in Python dictionary
    ###########################################################################################

    mars_data_dict = {}

    mars_data_dict['news_title'] = latest_news_title
    mars_data_dict['news_paragraph'] = latest_news_paragraph
    mars_data_dict['featured_image_url'] = featured_image_url

    mars_facts = mars_facts_df.to_html(header=True, index=True)
    mars_data_dict['mars_facts'] = mars_facts

    mars_data_dict['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_data_dict