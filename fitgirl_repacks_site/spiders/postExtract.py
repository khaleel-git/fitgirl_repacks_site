from socket import TIPC_DEST_DROPPABLE
from urllib.parse import non_hierarchical
import scrapy
import json
import time
import sys


class PostextractSpider(scrapy.Spider):
    name = 'postExtract'
    allowed_domains = ['fitgirl-repacks.site']
    start_urls = ['https://fitgirl-repacks.site/road-maintenance-simulator/']

    def parse(self, response):
        print(response.request.headers.get("User-Agent"))
        f = open('postsLinks.json')
        data = json.load(f)
        count = 0
        for i in data:
            count = count + 1
            # print(i['link'])          
            link = i['link']
            # print(link)
            yield scrapy.Request(response.urljoin(link),callback=self.parse_details)
            print(" ")
            print(f"############################# Processing Post = {count} #############################")
            print(" ")
            # if (count == 5):
                # break
        

    
    def parse_details(self, response):
        # address_parts = response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/p[1]//text()').getall()
        # address_parts = [sh.cleanup(x) for x in address_parts]

        # Name = response.css('.text-sfma ::text').get()
        # Address = ', '.join(address_parts)
        # Phone = sh.cleanup(response.xpath('//strong[text()="Tel:"]/../text()').get())
        # Fax = sh.cleanup(response.xpath('//strong[text()="Fax:"]/../text()').get())
        # Email = sh.cleanup(response.xpath('//strong[text()="Email:"]/../text()').get())
        # Website = sh.cleanup(response.xpath('//strong[text()="Website:"]/../text()').get())
        # print("hello i am in parse_details function")
        # time.spleep(1)

        #initializing variables
        post_link = None
        screenshot_featured_img = None
        cat = None
        img = None
        title = None

        try:
            content = response.xpath('//*/article/div').extract()  
            content = content[0]
            # print(content)    
            content = content.replace('\n','')
            content = content.replace('\t','')
            content = content.replace('&nbsp;', '')


            content = content.replace('style="height: 200px; display: block;"', '') 

            set_first_img = response.xpath('//*/article/div/p[1]/a').extract()
            set_first_img =  set_first_img[0]
            set_first_img_position = "<div>" + set_first_img + "</div>"

            content = content.replace(set_first_img, set_first_img_position)
            content = content.replace('<p></p>','&nbsp;<div>&nbsp;</div>')



            # content = content.replace('<h3>Download Mirrors</h3>', '<h3>Download Mirrors</h3>')
            content = content.replace('Game Description','<h2>Game Description</h2>')
            content = content.replace('MISSIONS:', '<h4>MISSIONS:</h4>')
            content = content.replace('VEHICLES:', '<h4>VEHICLES:</h4>')
            content = content.replace('Game Features', '<h3>Game Features</h3>')
            

            # remove styles
            content = content.replace('class="entry-content"', '')
            content = content.replace('class="su-spoiler su-spoiler-style-fancy su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no"', '')
            content = content.replace('class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span>', '')
            content = content.replace('class="su-spoiler-content su-u-clearfix su-u-trim"', '')

            # fix div tags
            content = content.replace('<div <h2>', '<div><h2>')
            content = content.replace('<!--', '<!--  ')
            content = content.replace('-->', '  -->')
            # content = content.replace('< >', '')
            # content = content.replace('<>', '')

            # #some <, <!-- and --> annomalies
            # # content = content.replace('< <h2>Game Description</h2>', '<h2>Game Description</h2>')
            # content = content.replace('< ', '')
            # content = content.replace('<!--<li>', '<li>')
            # content = content.replace('</li>-->', '</li>')
        except Exception as ex:
            # time.sleep(1)
            print(ex)

       
        try:
            fancy_title = response.xpath('//*/article/div/h3[1]').extract()
            fancy_title = fancy_title[0]
            print(fancy_title)
        except Exception as ex:
            # time.sleep(1)
            print(ex)
        
        try:
            title = response.xpath('//*/article/header/h1/text()').extract()
            title = title[0]
            print(title)
        except Exception as ex:
            # time.sleep(1)
            print(ex)

        
        try:
            #convert title to h2
            non_fancy_title = '<h2>' + title + '</h2>'

            print(non_fancy_title)

            content = content.replace(fancy_title, non_fancy_title)
        except Exception as ex:
            # time.sleep(1)
            print(ex)

        # try:
        #     #remove this image -> it is causing issue on mobile devices
        #     info_img = response.xpath('//*/article/div/ul/li[1]/img ').extract()
        #     info_img = info_img[0]
        #     content = content.replace(info_img, '')
            
        #     # print(content)
        # except Exception as ex:
        #     # time.sleep(1)
        #     print(ex)


        try:  
            #these are first and second images for featured image         
            first_img = response.xpath('//*/article/div/p[1]/a/img/@src').extract()
            first_img = first_img[0]

            screenshot_featured_img = response.xpath('//*/article/div/p[4]/a/img/@src').extract()
            screenshot_featured_img = screenshot_featured_img[0]

            post_link = str(response)
            post_link = post_link.split(' ')[1]
            post_link = post_link.split('>')[0]
        except Exception as ex:
            # time.sleep(1)
            print(ex)

        try:
            data =  { "link": post_link, "title":title, "first_img": first_img, "second_img": screenshot_featured_img, "body": content}
        except Exception as ex:
            # time.sleep(1)
            print(ex)
            time.sleep(1)

        try:
            title_with_dashes = title.replace(' ','-')
            
            with open('content/' + title_with_dashes + '.json', 'w') as fd:              
                json.dump(data,  fd, indent = 4) 
        except Exception as ex:
            # time.sleep(1)
            print(ex)
            
        
    

