from pprint import pprint

#导入自动化模块
from DrissionPage import ChromiumPage
#导入csv模块
import csv
#创建文件对象
f = open('data.csv', mode='w', encoding='utf-8',newline='')
#字典写入方法
csv_writer = csv.DictWriter(f,fieldnames=[
    '职位', '城市', '区域', '街道', '公司', '薪资', '经验', '学历', '领域', '融资', '规模', '技能要求', '基本福利'
])
#写入表头
csv_writer.writeheader()
#实例化浏览器对象（自动打开浏览器）
dp = ChromiumPage()
#监听数据包
dp.listen.start('wapi/zpgeek/search/joblist.json')
#访问网站
dp.get("https://www.zhipin.com/web/geek/job?query=python&city=100010000")
#等待数据包加载
resp = dp.listen.wait()
#获取数据包
json_data = resp.response.body
"""解析数据"""
#取职位信息所在列表
jobList = json_data['zpData']['jobList']
##for循环遍历，提取列表里面元素（30个岗位信息）
for index in jobList:
    #提取职位信息数据，保存字典
    dit = {
       '职位': index['jobName'],
        '城市': index['cityName'],
        '区域': index['areaDistrict'],
        '街道': index['businessDistrict'],
        '公司': index['brandName'],
        '薪资': index['salaryDesc'],
        '经验': index['jobExperience'],
        '学历': index['jobDegree'],
        '领域': index['brandIndustry'],
        '融资': index['brandStageName'],
        '规模': index['brandScaleName'],
        '技能要求': ''.join(index['skills']),
        '基本福利': ''.join(index['welfareList']),
    }
    # 写入数据
    csv_writer.writerow(dit)
    print(dit)