# -*- coding:utf-8 -*-
import yaml
with open("search_page.yaml",'r',encoding='utf-8') as f:
    data=yaml.load(f)
    print(type(data))  #打印data类型
    print(data)    #d打印data返回值