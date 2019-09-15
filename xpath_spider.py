import requests
import time
import re
import os
from lxml import etree
import pickle as pk
from csv import DictWriter
import time

url = "https://www.qichacha.com/firm_576c21e3468a6b178bbf291e4820e896.html"
ulist = []


def write2csv(info_dict, province):
    try:
        fieldnames = ['com_name', 'province', 'city', 'credit_no', 'legal_person', 'com_type', 'com_cate', 'data_eastablish', 'capital', 'num_emp', 'locate', 'bussiness_scope', 'url']
        if os.path.exists('./data/' + province + '.csv'):
            flag = 1
        else:
            flag = 0
        with open('./data/' + province + '.csv', 'a', newline='', encoding='UTF-8') as f:
            f_csv = DictWriter(f, fieldnames=fieldnames)
            if flag == 0:
                f_csv.writeheader()
            else:
                pass
            f_csv.writerow(info_dict)
    except Exception as e:
        print(e)


def parse_page(url, province, city_code):
    """
    解析最终公司信息页面
    """
    info_dict = {}
    try:
        time.sleep(5)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'CooKie': 'UM_distinctid=16d217b3855349-0c11a1081f70758-4c312373-1fa400-16d217b38563ca; CNZZDATA1254842228=226360575-1568220208-https%253A%252F%252Fwww.baidu.com%252F%7C1568529241; zg_did=%7B%22did%22%3A%20%2216d217b39cd40-0b50f0997e2be-4c312373-1fa400-16d217b39ce4d2%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201568531054521%2C%22updated%22%3A%201568531404161%2C%22info%22%3A%201568224786904%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%225bd1ab74caa9a464f464ed95fc9cccd1%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1568527694,1568527720,1568527741,1568528091; _uab_collina=156822478809561064355813; acw_tc=2ff6059815682247905453979e3bff64f9486aee8fb5577df85ca2091c; QCCSESSID=rphgi2rmo848070upokfa97pa1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1568531062; hasShow=1',
        }
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)

        table = selector.xpath('.//section[@id="Cominfo"]/table')[0]

        print("====================================================================")
        print("")

        # 公司名称
        com_name = selector.xpath('.//div[@class="row title jk-tip"]/h1/text()')[0]
        print(com_name)

        # 省份 todo 所属地区？？
        province = table.xpath('//tr[8]/td[2]/text()')[0].strip()
        print(province)

        # 城市
        citycode_2_CN = pk.load(file=open('./data/citycode_2_CN.pkl', 'rb'))
        city = citycode_2_CN[str(city_code)]
        print(city)

        # 信用代码
        credit_no = table.xpath('//tr[4]/td[2]/text()')[0].strip()
        print(credit_no)

        #  法定代表人
        legal_person = table.xpath('//tr[1]//h2/text()')[0].strip()
        print(legal_person)

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
        pass

        # 经营范围
        bussiness_scope = table.xpath('//tr[12]//td[2]/text()')[0].strip()
        print(bussiness_scope)

        # 网址
        if selector.xpath('.//div[@class="dcontent"]/div[1]/span[3]/a/text()'):
            url = selector.xpath('.//div[@class="dcontent"]/div[1]/span[3]/a/text()')[0].strip()
        else:
            url = '-'
        print(url)

        # 电话号码
        pass

        # 更多号码
        pass

        info_dict['com_name'] = com_name
        info_dict['province'] = province
        info_dict['city'] = city
        info_dict['credit_no'] = credit_no
        info_dict['legal_person'] = legal_person
        info_dict['com_type'] = com_type
        info_dict['com_cate'] = com_cate
        info_dict['data_eastablish'] = data_eastablish
        info_dict['capital'] = capital
        info_dict['num_emp'] = num_emp
        info_dict['locate'] = locate
        info_dict['bussiness_scope'] = bussiness_scope
        info_dict['url'] = url

        """
        如果公司人数大于500，写入CSV
        """
        if re.search(r'[\d]+', info_dict['num_emp']):
            num_emp = int(re.search(r'[\d]+', info_dict['num_emp']).group())
            if num_emp >= 500:
                print("公司的人数有:", info_dict['num_emp'], "写入数据")
                write2csv(info_dict, province)

    except Exception as e:
        print(e)


def parse_columns(province="AH", city_code=340100):
    """
    解析地区的选择翻页界面
    """
    for i in range(1, 501):
        time.sleep(2)
        print("下面爬取第%d页内容" % i)
        print("*********************")
        url = 'https://www.qichacha.com/gongsi_area.html?prov=' + province + '&city=' + str(city_code) + '&p=' + str(i)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'cookie': 'UM_distinctid=16d217b3855349-0c11a1081f70758-4c312373-1fa400-16d217b38563ca; CNZZDATA1254842228=226360575-1568220208-https%253A%252F%252Fwww.baidu.com%252F%7C1568523841; zg_did=%7B%22did%22%3A%20%2216d217b39cd40-0b50f0997e2be-4c312373-1fa400-16d217b39ce4d2%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201568527086337%2C%22updated%22%3A%201568528174408%2C%22info%22%3A%201568224786904%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%225bd1ab74caa9a464f464ed95fc9cccd1%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1568527694,1568527720,1568527741,1568528091; _uab_collina=156822478809561064355813; acw_tc=2ff6059815682247905453979e3bff64f9486aee8fb5577df85ca2091c; QCCSESSID=rphgi2rmo848070upokfa97pa1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1568528175; hasShow=1'
        }
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)

        table = selector.xpath('.//table[@class="m_srchList"]//tr/td[2]/a/@href')
        for j in table:
            company_url = 'https://www.qichacha.com' + j
            print(company_url)
            parse_page(company_url, province, city_code)


if __name__ == '__main__':
    parse_columns()
