
import urllib.request
import json
if __name__ == '__main__':
    print("搜索音乐")
    searchMusicUrl = "http://tingapi.ting.baidu.com/v1/restserver/ting"

    searchParam = "format=json&calback=&from=webapp_music&method=baidu.ting.search.catalogSug&query=邓紫棋"

    opener = urllib.request.build_opener()
    data = opener.open(fullurl=searchMusicUrl, data=bytes(searchParam, encoding="utf8")).read()

    myjson = json.loads(data)
    result = json.dumps(myjson, ensure_ascii=False)
    print(result)
