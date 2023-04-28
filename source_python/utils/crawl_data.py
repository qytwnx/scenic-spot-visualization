import time
import requests
import parsel
import csv
import json
from fake_useragent import UserAgent

f = open('旅游景点.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f,
                            fieldnames=['name', 'level', 'province', 'city', 'address', 'heat', 'introduction',
                                        'price', 'sales', 'image', 'info', 'comment'])

csv_writer.writeheader()

cookie = 'QN1=00007080306c4f706e78213d; QN300=s%3Dbing; QN99=9808; QunarGlobal=10.67.200.16_22579bf7_187787acaa7_1ddd|1681360848162; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN205=s%3Dbing; QN277=s%3Dbing; csrfToken=1qP917vmdPHHpNQlCP3R9fMTywgta9I2; _i=VInJOmJqqqwqkNFqY57Hf2bl6f6q; QN601=1ddc5c2706632e98414364744772ba77; QN163=0; QN269=5CDF9D20D9B511EDA154FA163E3ACAE1; fid=0d1a7c02-6c2b-46e9-85dc-5b4e8a74aa0b; QN48=tc_d910ee0b942910dc_18778ea889d_7518; ariaDefaultTheme=null; quinn=c6cae945b52143d2e2ac7fbf9a2fdc6b5c52b819894f42fbc4831d508816a3d2fc0cdc4827d8b28a9194fb96ce2b1b16; QN57=16813609268590.3943675580371728; QN5=qunar_tjmp; Hm_lvt_15577700f8ecddb1a927813c81166ade=1681360927; QN71="MTI0LjE1Mi4yNTQuODg65YWw5beeOjE="; QN67=513949%2C38170; _vi=nQfyQ2FUrQGyuwR6UYhJX-4xOatw4M0EPODbB0Ewvc0LqndjHPgk44oZJKBP1jLmaSiPVftFy-4BU17sqZ9_vB49S3IXCCzRGJ_zW4Eht-34y4QiC8z3SqpxcVxwu6-ucjvl3G7WWntanjrq3Gy_Jw7LX6knlxFvSixqx_I1oIGz; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1681365469; QN271=ffd282f3-e521-4952-bd41-7409cb842742; __qt=v1%7CVTJGc2RHVmtYMTl3WWNQNXJ2L0pJYjJPZk0yY3d4RWg5eklRQ2gzK05JUytnREp2UXlJL1FoSUZFSlovQWRPVGkxeDY1U2pibCtKZVA3cGRWR2RMN0hyQ09oa2RaQUs4UVFOcjRxOHBuTzEyMytTeVRTTGxNcUlMUllPNnBiNk83N2Ixc1BZNzNNL3E3WjNFQjBYQ1FNaUwyMDVuOCt5dUhMQXJER3hycVpjPQ%3D%3D%7C1681365602128%7CVTJGc2RHVmtYMTlHMXhUY1VBbWJsbVk0Q3VGY1RJZit5WmRRamNOWTBsWmN5Y3drdCtUWmpzQmJvTzVhanpwaFloNGthclBReGl4NzY5WVRqYTk5SFE9PQ%3D%3D%7CVTJGc2RHVmtYMTlWb2UzdlFGMGhZS2V5c3FralJ2cUgxQTRreUJnM1J1Z3VKY3JtWm81aWczRS9ZREVoNFYxYm5UVW14bVZObCtHdDFsVzVwbGJ5QUUxWEpHK2h1ZUNRL2JYajE0QXBQUEg1WUhhTWdHL3UyQU5NT1VWZVAvSGF0aFUvZTBVZWxMU2d5OGJkWFZ1N3diY3ZMS3FjYS9YMi9BN013czBLZlNYL09peGVFazFWVnA5bkYyL0ZiMFNrSWYrRWk5aDlCdUN5WkxicGpuUi8yVi8zclFFQlJuMDB3cnJMV2liK092MFl1YmwxTFlQaHpsbjhTV0RpWjNFS0tBaW5IeG96Z2tJMW1aUzgyUmdnS2p6UzBadmJFK3FIRXowQTNPemk4QW84WDUrb01GcEV1NU1sQkJvdUJ0NVlBSGNTMUhnbTVPYTV1ck1JZkpRanNRNWNnc3pYQ0NTb0tZWFJDMEx5d3NiYnNkNUJ6RVdEbGNZNEF3eFF1WExCaGgyNVFjYjl3QmZLcHNXYmhWR29YL2hwamdpSUswU3RQd29jbTdlZ3lnUEljLzFIVW5FbXE4b0xac0wyRzQwWFlwR2FERmZHVSt4bFM1ZjJ5QkFtZDdKcGhtdHlFZHNuRTdCTk1JeDBCazEzQzJDN2xCYndaZktNUk1rSmdnNDNLaWNJdC9aaVJNQnI2NUtSdHNIdzllVlVUV0tFQWVNWkQ3RFpaMHNwMXd4a0taNnRGWHA1UmlxaHl1YW5XaHhSaE5hL3dXM2lMcXhRb1RnaGd6OG13TjV6NzEvWU5QWVpCY2lrVmtjMUxMdUxmdlg0cGdKY1ozTmxhajlTV25DTWpJVU9HYWpuNnl1T3ozWTFmSjVSZ29kaDgvZUZIcUE0NEFaRVA2cCtJSFZZMkMwS3BZSGR6aTR5c2Rjd1pkd2c%3D; JSESSIONID=90409EEDC8F50333333BDFAE4101874B; QN267=849812934d3935277; QN58=1681365335014%7C1681365604093%7C3'
ua = UserAgent()

page = 99

while True:
    print(
        '====================================正在保存第{}页数据=================================='.format(page))
    url = 'https://piao.qunar.com/ticket/list_中国.html?from=mps_search_suggest_c&keyword=中国&page={}'.format(page)
    headers = {
        'user-agent': ua.random,
        'Cookie': cookie,
    }
    response = requests.get(url=url, headers=headers)
    if str(response) == '<Response [404]>':
        continue
    selector = parsel.Selector(response.text)
    lis = selector.css('#search-list .sight_item')
    dit = {}
    for li in lis:
        title = li.css('.sight_item_caption a::attr(title)').get()  # 景区名字
        dit['name'] = title.strip()
        d_url = li.css('.sight_item_caption a::attr(href)').get()  # 详情
        detail_url = 'https://piao.qunar.com' + d_url
        res = requests.get(url=detail_url, headers=headers)
        if str(res) == '<Response [404]>':
            continue
        sel = parsel.Selector(res.text)
        info = sel.css('.mp-charact-content .mp-charact-desc p::text').get()
        dit['info'] = info.strip()
        try:
            dit['info'] = info.strip()
        except:
            dit['info'] = info
        comm = sel.css('.mp-comments-head a::attr(href)').get()
        sightId = comm.split('=')[-1]
        comm_url = f'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId={sightId}&index=1&page=1&pageSize=10&tagType=0'
        comm_content = ''
        comm_res = requests.get(url=comm_url, headers=headers)
        if str(comm_res) == '<Response [404]>':
            continue
        try:
            comm_json = json.loads(comm_res.text)
            comm_content = comm_json['data']['commentList'][0]['content']
        except:
            comm_content = '暂未评价'
        dit['comment'] = comm_content

        image_url = li.css('.sight_item_show img::attr(data-original)').get()
        dit['image'] = image_url.strip()

        level = li.css('.sight_item_info .level::text').get()  # 景区等级
        if level is None:
            level = '暂未评级'
        dit['level'] = level
        area = li.css('.area a::attr(title)').get()  # 地区
        dit['province'] = area.split('·')[0] + '省'
        dit['city'] = area.split('·')[1] + '市'
        address = li.css('.address span::attr(title)').get()  # 地址
        dit['address'] = address.strip()
        string = li.css('.product_star_level em::attr(title)').get()  # 热度
        star_level = float(string.strip('热度: '))
        dit['heat'] = star_level
        intro = li.css('.intro::attr(title)').get()  # 简介
        dit['introduction'] = intro
        price = li.css('.sight_item_price em::text').get()  # 价格
        dit['price'] = price
        hot_num = li.css('.hot_num::text').get()  # 月销
        dit['sales'] = hot_num
        csv_writer.writerow(dit)
        print(dit)
    if page == 334:
        break
    if page % 2 == 0:
        time.sleep(240)
    page += 1
