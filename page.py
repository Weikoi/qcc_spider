import requests
import time
import re
from lxml import etree
import pickle as pk
from collections import OrderedDict

url = "https://www.qichacha.com/g_AH.html"
ulist = []


# /html/body/div[4]/div[2]/div[1]/div/section[3]/table/tbody/tr[4]/td[2]
def parse_page(url):
    province_city_dict = OrderedDict()
    citycode_2_CN = {}
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

        }
        html = requests.get(url, headers=headers).text
        print(html)
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
            city_names = selector_.xpath(
                './/div[@class="col-md-12 no-padding-right"]/div[2]//div[@class="pills-after"]/a/text()')
            city_code = [re.split(r"\.|_", i)[2] for i in city_urls]
            print(city_code)
            print(city_names)
            for j in range(len(city_code)):
                citycode_2_CN[city_code[j]] = city_names[j]
            province = re.split(r"\.|_", i)[1]
            province_city_dict[province] = city_code
        print(province_city_dict)
        print(citycode_2_CN)
        # print(province_city_dict['AH'])
        pk.dump(province_city_dict, file=open('./data/province_city_dict.pkl', 'wb'))
        pk.dump(citycode_2_CN, file=open('./data/citycode_2_CN.pkl', 'wb'))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    parse_page(url)
