
import requests
import json

def fetchweather(location):
    d={'key':'btqi3ahf1rsicuur',
    'location':location,
    'language':'zh-Hans',
    'unit':'c'}
    r = requests.get('https://api.seniverse.com/v3/weather/now.json',params=d)
    weather = json.loads(r.text)
    return weather
# 从API中获取数据


print("请输入指令或者您要查询的城市名：")

history = []


while True:
      user_input =input('> ')
      if user_input == 'quit' or user_input == 'q':
           exit(0)
      elif user_input == 'help' or user_input == '?':
           print('''
        输入城市名，查询该城市天气；
        输入 help，获取帮助文档；
        输入 history，获取查询历史；
        输入 quit，退出天气查询系统。
        ''')
      elif user_input == 'history':
         print(history)
      elif 'status' in fetchweather(user_input):
         print("对不起没有改地方天气资料")
      elif 'results' in fetchweather(user_input):
         text = fetchweather(user_input)['results'][0]['now']['text']
         c = fetchweather(user_input)['results'][0]['now']['temperature']
         t = fetchweather(user_input)['results'][0]['last_update']
         print(f"{user_input}的天气为{text} 温度为{c}")
         print(f"更新时间:{t}")
         history.append(f"{user_input}天气{text} 温度{c} 更新时间{t}")
         #用API返回的内容判断是否正常获取数据,用键来判断

      else:
        print("恭喜你找到了BUG")
