import random
import json

locations = {
  'Chengdu': (30.5728, 104.0668),
  'Beijing': (39.9042, 116.4074),
  'Shanghai': (31.2304, 121.4737),
  'Taipei': (25.0330, 121.5654),
  'Dazhou': (31.2096, 107.4680),
  'Hong Kong': (22.3193, 114.1694),
  'Shenzhen': (22.5431, 114.0579),
  'Tokyo': (35.6762, 139.6502),
  'Seoul': (37.5665, 126.9780),
  'Tibet': (30.1534, 88.7879),
  'Hokkaido': (43.2203, 142.8635),
  'Sapporo': (43.0618, 141.3545),
  'Kyoto': (35.0116, 135.7681),
  'Saigon': (10.8231, 106.6297),
  'Hanoi': (21.0278, 105.8342),
  'Bangkok': (13.7563, 100.5018),
  'Vientiane': (17.9757, 102.6331),
  'Macau': (22.1987, 113.5439),
  'Hainan': (19.5664, 109.9497),
  'Urumqi': (43.8256, 87.6168),
  'Mumbai': (19.0760, 72.8777),
  'Osaka': (34.6937, 135.5023),
  'Chongqing': (29.4316, 106.9123),
  'Jiuquan': (39.7329, 98.4945),
  'Xian': (34.3416, 108.9398),
  'Hangzhou': (30.2741, 120.1551),
  'Guangzhou': (23.1291, 113.2664),
  'Hohhot': (40.8424, 111.7500),
  'Jinan:': (36.6512, 117.1201),
  'Wuhan': (30.5928, 114.3055),
  'Nanjing': (32.0603, 118.7969),
  'Wenzhou': (27.9938, 120.6994),
  'Fuzhou': (26.0745, 119.2965),
  'Qingdao': (36.0671, 120.3826),
  'Harbin': (45.8038, 126.5350),
  'Mohe': (52.9723, 122.5386)
}

names = [
  'aaa ff', 
  'bbb', 
  'ccc gg', 
  'xxx v', 
  'tyt iiii eeee', 
  'sss lkop wgw',
  'poppppppppp',
  'kjkjkjkjkjkjkjkjkjkjk',
  'zz xx cc vv',
  '一些中文',
  '长一些的句子哈哈',
  '再来一句更长很多很大的句子']

startTimes = [
  '1993-11-22',
  '1998-06-06',
  '1913-05-13',
  '1966-12-05',
  '1923-11-10',
  '1856-04-12',
  '1889-03-23',
  '1934-07-15',
  '1734-09-12',
  '1264-10-25',
  '1096-06-02',
  '1501-08-31',      
]

types = [
  'HISTORY_EVENT',
  'PERSON',
  'CHARACTER'
]

descriptions = [
  'this is a description about something',
  'lalala lalala lalala hahahahahahahaha',
  'ooooooooops, that is messed up',
  'once up a time, something happened',
  'the random data needs a really long description in order to take up as much space as it can',
  'this time it will try to continue creating an even larger text to occupy even more space to check whether there will be any layout odds shownup on the page'
]

def toMapItem(indexAndLocation):
  index, location = indexAndLocation
  city, coordinate = location
  latitude = coordinate[0]
  longitude = coordinate[1]
  name = random.choice(names)
  startTime = random.choice(startTimes)
  itemType = random.choice(types)
  desc = random.choice(descriptions)
  return {
    'name': str(index + 1) + ' ' + name,
    'type': itemType,
    'location': {
      'latitude': latitude,
      'longitude': longitude,
      'city': city
    },
    'period': {
      'startTime': startTime
    },
    'options': {
      'description': desc
    }
  }

mapItems = list(map(toMapItem, enumerate(list(locations.items()))))
data = {
  'mapItems': mapItems
}

with open('randomDb.json', 'w', encoding='utf-8') as f:
  json.dump(mapItems, f, ensure_ascii=False, indent=2)

