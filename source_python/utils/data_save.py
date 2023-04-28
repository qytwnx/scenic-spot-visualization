import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@8.130.116.227:3306/match_database")

df = pd.read_csv('旅游景点.csv')

# 1.修改北京
df.province[df.province == '北京省'] = "北京市"
df.loc[df.city == '北京市', 'city'] = df.loc[df.city == '北京市', 'address'].str[3:6]
df.loc[(df.province == '北京市') & (df.city == '西直门'), 'city'] = '西城区'
df.loc[(df.province == '北京市') & (df.city == '物院宁'), 'city'] = '东城区'
df.loc[(df.province == '北京市') & (df.city == '香山卧'), 'city'] = '海淀区'
df.loc[(df.province == '北京市') & (df.city == '街4号'), 'city'] = '东城区'
df.loc[(df.province == '北京市') & (df.city == '门头沟'), 'city'] = '门头沟区'
df.loc[(df.province == '北京市') & (df.city == '街17'), 'city'] = '西城区'
df.loc[(df.province == '北京市') & (df.city == '怀北镇'), 'city'] = '怀柔区'
df.loc[(df.province == '北京市') & (df.city == '花乡丰'), 'city'] = '丰台区'
df.loc[(df.province == '北京市') & (df.city == '中华路'), 'city'] = '东城区'
df.loc[(df.province == '北京市') & (df.city == '区潭柘'), 'city'] = '门头沟区'
df.loc[(df.province == '北京市') & (df.city == '西三环'), 'city'] = '海淀区'
df.loc[(df.province == '北京市') & (df.city == '龙潭路'), 'city'] = '东城区'
df.loc[(df.province == '北京市') & (df.city == '白马路'), 'city'] = '顺义区'
df.loc[(df.province == '北京市') & (df.city == '镇水头'), 'city'] = '房山区'
df.loc[(df.province == '北京市') & (df.city == '王佐镇'), 'city'] = '丰台区'

# 2.修改天津市
df.province[df.province == '天津省'] = "天津市"
df.loc[df.city == '天津市', 'city'] = df.loc[df.city == '天津市', 'address'].str[3:6]
df.loc[(df.province == '天津市') & (df.city == '滨海新'), 'city'] = '滨海新区'
df.loc[(df.province == '天津市') & (df.city == '蓟县官'), 'city'] = '蓟州区'
df.loc[(df.province == '天津市') & (df.city == '蓟县城'), 'city'] = '蓟州区'
df.loc[(df.province == '天津市') & (df.city == '静海县'), 'city'] = '静海区'
df.loc[(df.province == '天津市') & (df.city == '黄崖关'), 'city'] = '蓟州区'
df.loc[(df.province == '天津市') & (df.city == '蓟县津'), 'city'] = '蓟州区'
df.loc[(df.province == '天津市') & (df.city == '鞍山道'), 'city'] = '和平区'

# 5.修改内蒙古自治区
df.province[df.province == '内蒙古省'] = "内蒙古自治区"
df.loc[(df.province == '内蒙古自治区') & (df.city == '锡林郭勒盟市'), 'city'] = '锡林郭勒盟'

# 7.修改吉林省
df.loc[(df.province == '吉林省') & (df.city == '延边市'), 'city'] = '延边朝鲜族自治州'
df.loc[(df.province == '吉林省') & (df.city == '吉林市市'), 'city'] = '吉林市'

# 8.修改黑龙江省
df.loc[(df.province == '黑龙江省') & (df.city == '大兴安岭市'), 'city'] = '大兴安岭地区'

# 9.修改上海市
df.province[df.province == '上海省'] = "上海市"
df.loc[df.city == '上海市', 'city'] = df.loc[df.city == '上海市', 'address'].str[3:6]
df.loc[(df.province == '上海市') & (df.city == '浦东新'), 'city'] = '浦东新区'
df.loc[(df.province == '上海市') & (df.city == '中山东'), 'city'] = '黄浦区'
df.loc[(df.province == '上海市') & (df.city == '人民大'), 'city'] = '黄浦区'
df.loc[(df.province == '上海市') & (df.city == '区锦绣'), 'city'] = '浦东新区'
df.loc[(df.province == '上海市') & (df.city == '北沿公'), 'city'] = '崇明区'
df.loc[(df.province == '上海市') & (df.city == '沪杭公'), 'city'] = '金山区'
df.loc[(df.province == '上海市') & (df.city == '浦东卓'), 'city'] = '浦东新区'
df.loc[(df.province == '上海市') & (df.city == '海湾镇'), 'city'] = '奉贤区'
df.loc[(df.province == '上海市') & (df.city == '虹梅路'), 'city'] = '闵行区'
df.loc[(df.province == '上海市') & (df.city == '金商公'), 'city'] = '青浦区'
df.loc[(df.province == '上海市') & (df.city == '佘山塔'), 'city'] = '松江区'
df.loc[(df.province == '上海市') & (df.city == '区陆家'), 'city'] = '浦东新区'
df.loc[(df.province == '上海市') & (df.city == '服务亭'), 'city'] = '浦东新区'
df.loc[(df.province == '上海市') & (df.city == '枫泾镇'), 'city'] = '金山区'
df.loc[(df.province == '上海市') & (df.city == '江区辰'), 'city'] = '松江区'
df.loc[(df.province == '上海市') & (df.city == '海涵路'), 'city'] = '奉贤区'
df.loc[(df.province == '上海市') & (df.city == '绿华镇'), 'city'] = '崇明区'

# 20.修改广西壮族自治区
df.province[df.province == '广西省'] = "广西壮族自治区"

# 21.修改海南省
df.loc[(df.province == '海南省') & (df.city == '保亭黎族苗族自治县市'), 'city'] = '保亭黎族苗族自治县'
df.loc[(df.province == '海南省') & (df.city == '定安市'), 'city'] = '定安县'
df.loc[(df.province == '海南省') & (df.city == '陵水黎族自治县市'), 'city'] = '陵水黎族自治县'

# 22.修改重庆市
df.province[df.province == '重庆省'] = "重庆市"
df.loc[df.city == '重庆市', 'city'] = df.loc[df.city == '重庆市', 'address'].str[3:6]
df.loc[(df.province == '重庆市') & (df.city == '九龙坡'), 'city'] = '九龙坡区'
df.loc[(df.province == '重庆市') & (df.city == '万盛区'), 'city'] = '綦江区'
df.loc[(df.province == '重庆市') & (df.city == '铜梁南'), 'city'] = '铜梁区'
df.loc[(df.province == '重庆市') & (df.city == '酉阳县'), 'city'] = '酉阳土家族苗族自治县'
df.loc[(df.province == '重庆市') & (df.city == '舟白街'), 'city'] = '黔江区'
df.loc[(df.province == '重庆市') & (df.city == '石柱土'), 'city'] = '石柱土家族自治县'
df.loc[(df.province == '重庆市') & (df.city == '潼南县'), 'city'] = '潼南区'
df.loc[(df.province == '重庆市') & (df.city == '沙坪坝'), 'city'] = '沙坪坝区'
df.loc[(df.province == '重庆市') & (df.city == '武隆县'), 'city'] = '武隆区'
df.loc[(df.province == '重庆市') & (df.city == '彭水县'), 'city'] = '彭水苗族土家族自治县'
df.loc[(df.province == '重庆市') & (df.city == '川区茶'), 'city'] = '永川区'
df.loc[(df.province == '重庆市') & (df.city == '夔门街'), 'city'] = '奉节县'
df.loc[(df.province == '重庆市') & (df.city == '双路镇'), 'city'] = '丰都县'
df.loc[(df.province == '重庆市') & (df.city == '区丰都'), 'city'] = '丰都县'
df.loc[(df.province == '重庆市') & (df.city == '大渡口'), 'city'] = '大渡口区'
df.loc[(df.province == '重庆市') & (df.city == '-南岸'), 'city'] = '南岸区'
df.loc[(df.province == '重庆市') & (df.city == '江区万'), 'city'] = '綦江区'
df.loc[(df.province == '重庆市') & (df.city == '区巫溪'), 'city'] = '巫溪县'

# 23.修改四川省
df.loc[(df.province == '四川省') & (df.city == '阿坝藏族羌族自治州市'), 'city'] = '阿坝藏族羌族自治州'
df.loc[(df.province == '四川省') & (df.city == '甘孜州市'), 'city'] = '甘孜藏族自治州'

# 24.修改贵州省
df.loc[(df.province == '贵州省') & (df.city == '黔东南市'), 'city'] = '黔东南苗族侗族自治州'
df.loc[(df.province == '贵州省') & (df.city == '黔南市'), 'city'] = '黔南布依族苗族自治州'
df.loc[(df.province == '贵州省') & (df.city == '黔西南市'), 'city'] = '黔西南布依族苗族自治州'

# 25.修改云南省
df.loc[(df.province == '云南省') & (df.city == '西双版纳市'), 'city'] = '西双版纳傣族自治州'
df.loc[(df.province == '云南省') & (df.city == '大理市'), 'city'] = '大理白族自治州'
df.loc[(df.province == '云南省') & (df.city == '迪庆市'), 'city'] = '迪庆藏族自治州'
df.loc[(df.province == '云南省') & (df.city == '德宏市'), 'city'] = '德宏傣族景颇族自治州'
df.loc[(df.province == '云南省') & (df.city == '红河市'), 'city'] = '红河哈尼族彝族自治州'
df.loc[(df.province == '云南省') & (df.city == '楚雄市'), 'city'] = '楚雄彝族自治州'

# 26.修改西藏自治区
df.province[df.province == '西藏省'] = "西藏自治区"

# 28.修改甘肃省
df.loc[(df.province == '甘肃省') & (df.city == '临夏市'), 'city'] = '临夏回族自治州'

# 29.修改青海省
df.loc[(df.province == '青海省') & (df.city == '海南藏族自治州市'), 'city'] = '海南藏族自治州'
df.loc[(df.province == '青海省') & (df.city == '海西蒙古族藏族自治州市'), 'city'] = '海西蒙古族藏族自治州'
df.loc[(df.province == '青海省') & (df.city == '海东地区市'), 'city'] = '海东地区'
df.loc[(df.province == '青海省') & (df.city == '海北藏族自治州市'), 'city'] = '海北藏族自治州'

# 30.修改宁夏回族自治区
df.province[df.province == '宁夏省'] = "宁夏回族自治区"

# 31.修改新疆维吾尔自治区
df.province[df.province == '新疆省'] = "新疆维吾尔自治区"
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '喀什市'), 'city'] = '喀什地区'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '昌吉市'), 'city'] = '昌吉回族自治州'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '博尔塔拉市'), 'city'] = '博尔塔拉蒙古自治州'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '克孜勒苏市'), 'city'] = '克孜勒苏柯尔克孜自治州'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '阿克苏地区市'), 'city'] = '阿克苏地区'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '伊犁市'), 'city'] = '伊犁哈萨克自治州'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '阿勒泰市'), 'city'] = '阿勒泰地区'
df.loc[(df.province == '新疆维吾尔自治区') & (df.city == '巴音郭楞市'), 'city'] = '巴音郭楞蒙古自治州'

# 33.修改香港特别行政区
df.province[df.province == '香港省'] = "香港特别行政区"
df.loc[df.city == '香港市', 'city'] = df.loc[df.city == '香港市', 'address'].str[3:6]
df.loc[(df.province == '香港特别行政区') & (df.city == '屿山香'), 'city'] = '荃湾区'
df.loc[(df.province == '香港特别行政区') & (df.city == '中环山'), 'city'] = '中西区'
df.loc[(df.province == '香港特别行政区') & (df.city == '龙西九'), 'city'] = '油尖旺区'

# 34.修改澳门特别行政区
df.province[df.province == '澳门省'] = "澳门特别行政区"
df.loc[df.city == '澳门市', 'city'] = df.loc[df.city == '澳门市', 'address'].str[3:6]
df.loc[(df.province == '澳门特别行政区') & (df.city == '氹体育'), 'city'] = '路凼填海区'

df.drop_duplicates(subset=['name'], keep='first')

df.to_sql(name='scenic_spots', con=engine, if_exists='append', index=False)
