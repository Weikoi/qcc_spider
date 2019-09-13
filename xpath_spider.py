import requests
import time
from lxml import etree
import pickle as pk

url = "https://www.qichacha.com/firm_576c21e3468a6b178bbf291e4820e896.html"
ulist = []


# /html/body/div[4]/div[2]/div[1]/div/section[3]/table/tbody/tr[4]/td[2]
def parse_page(url):
    pro_dicts_list = []
    question_content = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

        }
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)

        table = selector.xpath('.//section[@id="Cominfo"]/table')[0]

        # 名称
        com_name = selector.xpath('.//div[@class="row title jk-tip"]/h1/text()')[0]
        print(com_name)

        # 省份 todo 所属地区？？
        province = table.xpath('//tr[8]/td[2]/text()')[0].strip()
        print(province)

        # 城市 todo ???

        # 信用代码
        credit_no = table.xpath('//tr[4]/td[2]/text()')[0].strip()
        print(credit_no)

        #  法定代表人
        person = table.xpath('//tr[1]//h2/text()')[0].strip()
        print(person)

        #  企业类型
        com_type = table.xpath('//tr[6]/td[2]/text()')[0].strip()
        print(com_type)

        # 所属行业
        com_cate = table.xpath('//tr[6]/td[4]/text()')[0].strip()
        print(com_cate)

        # 成立日期
        data_eastablish = table.xpath('//tr[3]/td[4]/text()')[0].strip()
        print(data_eastablish)

        # 注册资本
        capital = table.xpath('//tr[1]/td[4]/text()')[0].strip()
        print(capital)

        # 企业人数
        num_emp = table.xpath('//tr[10]//td[2]/text()')[0].strip()
        print(num_emp)

        # 公司位置
        locate = table.xpath('//tr[11]//td[2]/text()')[0].strip()
        print(locate)

        # 邮箱

        # 经营范围
        bussiness_scope = table.xpath('//tr[12]//td[2]/text()')[0].strip()
        print(bussiness_scope)

        # 网址
        com_name = selector.xpath('.//span[@class="cvlu"]/a/text()')[0].strip()
        print(com_name)

        # 电话号码

        # 更多号码

        # table = selector.xpath('.//div[5]/ div[1] / table[2]/tbody/tr/td[2]/text()')
        # # title = selector.xpath('.//li[@class="jsk-active"]/text()')
        # for i in table[1:]:
        #
        #     print(i.encode("ISO-8859-1").decode("GBK"))
        #     ulist.append(i.encode("ISO-8859-1").decode("GBK"))
        # print(len(table[1:]))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parse_page(url)
    print(ulist)
    # pk.dump(ulist, file=open("./raw_data/985.pkl", 'wb'))
