import requests
import time
from lxml import etree
import pickle as pk
from collections import OrderedDict

url = "https://www.qichacha.com/g_AH.html"
ulist = []


# /html/body/div[4]/div[2]/div[1]/div/section[3]/table/tbody/tr[4]/td[2]
def parse_page(url):
    pro_dicts_list = []
    question_content = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

        }
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)

        province_urls = selector.xpath('.//div[@class="col-md-12 no-padding-right"]/div[1]//div[@class="pills-after"]/a/@href')
        print(province_urls)

        for i in province_urls:
            province_url = "https://www.qichacha.com" + i
            print(province_url)
            html_ = requests.get(province_url, headers=headers).text
            selector_ = etree.HTML(html_)
            city_urls = selector_.xpath(
                './/div[@class="col-md-12 no-padding-right"]/div[2]//div[@class="pills-after"]/a/@href')
            print(city_urls)



    except Exception as e:
        print(e)


if __name__ == '__main__':
    parse_page(url)
