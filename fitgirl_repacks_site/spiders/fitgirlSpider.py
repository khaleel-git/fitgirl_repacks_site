from ast import parse
from typing_extensions import Self
from pkg_resources import yield_lines
import scrapy
import time
import json


class FitgirlspiderSpider(scrapy.Spider):
    name = 'fitgirlSpider'
    allowed_domains = ['fitgirl-repacks.site']
    start_urls = ['https://fitgirl-repacks.site/']
    
    # headers = { "user_agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    
    def parse(self, response):
        pass
        # count = 0
        # for link in response.css("h1.entry-title a::attr(href)").getall():
        #     # time.sleep(1)
        #     item = {
        #         'link': link
        #     }           
        #     yield item

        # f = open('postsLinks.json')
        # data = json.load(f)
        # for i in data:
        #     print(i['link'])
        #     item = {
        #         'content': response.xpath('//*/article/div').extract()
        #     }
        #     # content = response.xpath('//*/article/div').extract()
        #     print("Now print the content")
        #     print(content)
        #     content = content.replace('\n','')
        #     content = content.replace('\t','')
        #     print(content)
        #     time.sleep(1)
        #     break

        # yield content
    

        # next_page = response.css("a.next.page-numbers").attrib["href"]
        # # count = count + 1
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


        

# f = open('postsLinks.json')
# data = json.load(f)
# for i in data:
#     print(i['link'])
#     time.sleep(1)

# content = """<div class="entry-content">

# \n\t\t
# <h3><span style="color: #339966;">#2660</span> <strong>Road Maintenance Simulator</strong></h3>
# \n
# <p style="height: 200px; display: block;"><a href="https://en.riotpixels.com/games/road-maintenance-simulator/" target="_blank" rel="noopener"><img class="alignleft" src="https://i3.imageban.ru/out/2022/04/11/8459fe2c1e5ec40a8263185681999be1.jpg" width="150" /></a>
# \nGenres/Tags: <strong>Lifestyle, First-person, Third-person, 3D</strong>
# \nCompanies: <strong>Caipirinha Games, Aerosoft GmbH</strong>
# \nLanguages: <strong>ENG/MULTI6</strong>
# \nOriginal Size: <strong>2.3 GB</strong>
# \nRepack Size: <strong>1.5 GB</strong></p>
# \n

# \n
# <h3>Download Mirrors</h3>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>\n
#  	<li><a href="https://1337x.to/torrent/5214482/Road-Maintenance-Simulator-MULTi6-FitGirl-Repack/" target="_blank" rel="noopener">1337x</a> | [<a href="magnet:?xt=urn:btih:EDE32A8D339B37B7607604E46F3F3B19B284736A&amp;dn=Road+Maintenance+Simulator+%28MULTi6%29+%5BFitGirl+Repack%5D&amp;tr=udp%3A%2F%2F46.148.18.250%3A2710&amp;tr=udp%3A%2F%2Fopentor.org%3A2710&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&amp;tr=http%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2730%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2770%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&amp;tr=http%3A%2F%2Fretracker.local%2Fannounce&amp;tr=http%3A%2F%2Fretracker.ip.ncnet.ru%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&amp;tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce">magnet</a>] [<a href="https://pastefg.hermietkreeft.site/?309d09332942657c#GpK1B6m9uyGZ4pwStPbTi4pujfKWS6cnynkob9QLX9Ji" target="_blank" rel="noopener">.torrent file only</a>]
# <img style="display: block; clear: both;" src="https://torrent-stats.info/04e4/17970624.png" /></li>
# </ul>
# </li>
# </ul>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>
#  	<li><a href="https://tapochek.net/viewtopic.php?p=2845412" target="_blank" rel="noopener">Tapochek.net</a></li>
# </ul>
# </li>
# </ul>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>
#  	<li><a href="https://pastefg.hermietkreeft.site/?598252dc67d199b7#WrkzEaEYtgUty1nNB32Y5ikShmigRAGLcHsN59gzLed" target="_blank" rel="noopener">Filehoster: MultiUpload</a> (10+ hosters, interchangeable) [Use <a href="http://jdownloader.org/jdownloader2" target="_blank" rel="noopener">JDownloader2</a>]</li>
# </ul>
# </li>
# </ul>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>
#  	<li><a href="https://pastefg.hermietkreeft.site/?a90fd48adcb15015#CMY6VzXDqubRTCPwUysb8xYe3xvNYDUytAsW5nNSZnTM" target="_blank" rel="noopener">Filehoster: ZippyShare</a></li>
# </ul>
# </li>
# </ul>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>
#  	<li><a href="https://pastefg.hermietkreeft.site/?7a9d976bde1c2ab3#DzyBjf24dLKPvZUbnmVTq8o3UBDyKsPqBPRBvHEpQRTn" target="_blank" rel="noopener">Filehoster: BayFiles</a></li>
# </ul>
# </li>
# </ul>
# \n
# <ul>
#  	<li style="list-style-type: none;">
# <ul>
#  	<li><a href="https://pastefg.hermietkreeft.site/?56362d1a3b5a8540#UV3K52xvuFtohbi1DNkXf9EFev2dxTjWxAi78zMiMkr" target="_blank" rel="noopener">Filehoster: OneDrive</a> (Uploaded by DyR0 t(-_-t), NOT compatible with other mirrors)</li>
# </ul>
# </li>
# </ul>
# \n

# <!--\n\n
#  	<li><a href="" target="_blank" rel="noopener">Filehosters: Google Drive, OneDrive + others</a> (Uploaded by crackhub213)</li>
# \n\n-->\n

# \n

# <a href="https://cs.rin.ru/forum/viewtopic.php?f=10&amp;t=121154" target="_blank" rel="noopener">Discussion and (possible) future updates on CS.RIN.RU thread</a>

# \n
# <h3>Screenshots (Click to enlarge)</h3>
# \n

# <a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/9/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/67/e8/67e8f2fc-820f-44a6-8042-8e83da9591fb.jpg.240p.jpg" width="178" height="100" border="0" /></a><a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/7/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/f7/56/f7561e72-6663-4455-9cc9-287da4044062.jpg.240p.jpg" width="178" height="100" border="0" /></a><a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/5/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/6b/28/6b28f068-52b7-4629-94a8-9fa7f8c1d303.jpg.240p.jpg" width="178" height="100" border="0" /></a>
# \n<a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/3/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/b7/9f/b79f61ae-dc1d-4eec-9dc3-4826367e0ac7.jpg.240p.jpg" width="178" height="100" border="0" /></a><a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/2/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/35/d8/35d8fccc-a1c5-49e6-9827-c64b1873aa6d.jpg.240p.jpg" width="178" height="100" border="0" /></a><a href="https://en.riotpixels.com/games/road-maintenance-simulator/screenshots/1/?utm_source=emb-gfx-html&amp;utm_medium=image&amp;utm_campaign=rp-mass" target="_blank" rel="noopener"><img src="https://s01.riotpixels.net/data/1d/c8/1dc8c6cb-6971-4ece-a2a6-576f89ccc95c.jpg.240p.jpg" width="178" height="100" border="0" /></a>

# \n
# <h3>Repack Features</h3>
# \n
# <ul>\n
#  	<li>Based on Road.Maintenance.Simulator-TiNYiSO ISO release: tn-roadmaintenancesimulator.iso (2,512,572,416 bytes)\n</li>
#  	<li>100% Lossless &amp; MD5 Perfect: all files are identical to originals after installation\n</li>
#  	<li>NOTHING ripped, NOTHING re-encoded\n</li>
#  	<li>Significantly smaller archive size (compressed from 2.3 to 1.5 GB)\n</li>
#  	<li>Installation takes 1-2 minutes (depending on your system)\n</li>
#  	<li>After-install integrity check so you could make sure that everything installed properly\n</li>
#  	<li>HDD space after installation: 2.4 GB\n</li>
#  	<li>Language can be changed in “Engine\\Binaries\\ThirdParty\\Steamworks\\Steamv151\\Win64\\steam_api.ini” file\n</li>
#  	<li>Repack uses XTool library by Razor12911\n</li>
#  	<li>At least 2 GB of free RAM (inc. virtual) required for installing this repack\n</li>
# </ul>
# \n
# <div class="su-spoiler su-spoiler-style-fancy su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
# <div class="su-spoiler-title" tabindex="0" role="button">Game Description</div>
# <div class="su-spoiler-content su-u-clearfix su-u-trim">

# \n

# Experience the everyday life in a German street maintenance service and complete a variety of realistic tasks in the area of road construction and maintenance! For your work you will have unique vehicles and various usable tools at your disposal.

# \n

# <b>MISSIONS:</b>
# \nNumerous tasks await you! In Street maintenance service, 30 extensive missions await you in a freely navigable road network. Complete a variety of exciting tasks in your daily work, including placing road markings, removing safety barriers, trimming trees, cleaning roadsides, installing traffic signs, crash barriers and delineators, and, of course, repairing roads.

# \n

# <b>VEHICLES:</b>
# \nChoose from a variety of vehicles! Drive in unique vehicles such as platform trucks and all-purpose vehicles in a freely drivable road network with highway, main and country road from your work yard to the site and complete your missions with combination roller and tar machine or even on foot!

# \n

# For your work you have various usable tools and objects at your disposal. Among them are motor vibrators, garbage gripper, cordless screwdrivers, signs, delineators and crash barriers.

# \n

# <b>Game Features</b>

# \n
# <ul>\n
#  	<li>30 extensive missions on the highway and main roads\n</li>
#  	<li>Freely drivable road network with freeway, main and country roads\n</li>
#  	<li>Walkable depot with fleet of vehicles and material warehouse\n</li>
#  	<li>More than 8 different road maintenance vehicles, such as bulldozer, all-purpose vehicle, road marking vehicle and dump truck\n</li>
#  	<li>Realistic tasks such as securing the work area, removing safety barriers, placing road markings, trimming trees, cleaning guard rails, cleaning roadsides, repairing roads, placing traffic signs, placing guard rails, placing delineators and much more\n</li>
#  	<li>Several objects for securing and completing the missions (from barks to guardrail to vibration dampers)\n</li>
#  	<li>Openworld map with interconnected road network\n</li>
#  	<li>Realistic graphics (Unreal Engine)\n</li>
# </ul>
# \n

# </div>
# </div>
# \n \t\t\n\t

# &nbsp;

# </div>"""

# content = content.replace('\n','')
# content = content.replace('\t','')
# content = content.replace('&nbsp;', '')
# content = content.replace('Game Description','<h3>Game Description</h3>')
# content = content.replace('MISSIONS:', '<h4>MISSIONS:</h4>')
# content = content.replace('VEHICLES:', '<h4>VEHICLES:</h4>')
# content = content.replace('Game Features', '<h3>Game Features</h3>')
# print(content)