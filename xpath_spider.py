import requests
import time
from lxml import etree
import pickle as pk

url = "https://www.qichacha.com/firm_ff3aac2898ef5e5f12f3d31032898c7c.html"
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

        table = selector.xpath('.//section[@id="Cominfo"]/table')[0]

        # 名称

        # 省份 todo 所属地区？？
        credit_no = table.xpath('//tr[8]/td[2]/text()')[0].strip()
        print(credit_no)

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
