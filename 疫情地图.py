# -*-coding：utf-8-*-
import requests
import json
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType, RenderType
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&'
data = json.loads(requests.get(url).json()['data'])
# html = (resp.json())
# time = json.loads(html['data'])
#print(data)
china = data['areaTree'][0]['children']
# print(china)
china_total = "确诊:" + str(data['chinaTotal']['confirm']) + \
            "疑似:" + str(data['chinaTotal']['suspect']) + \
            "死亡:" + str(data['chinaTotal']['dead']) + \
            "治愈:" + str(data['chinaTotal']['heal']) + \
            "更新日期:" + data['lastUpdateTime']


data = []
for i in range(len(china)):
    data.append([china[i]['name'],china[i]['total']['confirm']])
print(data)


geo = Geo(init_opts=opts.InitOpts(width="1900px",height="800px",bg_color="#404a59",page_title="全国疫情实时报告",renderer=RenderType.SVG,theme="white"))
geo.add_schema(maptype="china",itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)",border_color="rgb(0,0,0)"))
geo.add(series_name="",data_pair=data,type_=GeoType.EFFECT_SCATTER)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False),effect_opts=opts.EffectOpts(scale = 6))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=10,max_=549), title_opts=opts.TitleOpts(title="全国疫情地图",subtitle=china_total,pos_left="center",pos_top="10px",))
geo.render("render.html")


