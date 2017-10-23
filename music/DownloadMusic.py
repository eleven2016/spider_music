import urllib.request

if __name__ == '__main__':
    print("下载音乐")

    musicFile = "E:\\music\\2.mp3"

    #downloadUrl = "https://nj02all01.baidupcs.com/file/32a98c60d7326cca2ccf0715595595e2?bkt=p3-140032a98c60d7326cca2ccf0715595595e2ac8f24cd0000003302de&fid=3338965934-250528-1436207973&time=1506585437&sign=FDTAXGERLQBHSK-DCb740ccc5511e5e8fedcff06b081203-j8I7hZ5oYmBea0oQnG7aRrQAJkg%3D&to=69&size=3343070&sta_dx=3343070&sta_cs=2&sta_ft=mp3&sta_ct=7&sta_mt=7&fm2=MH,Nanjing02,Netizen-anywhere,,jiangsu,ct&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=140032a98c60d7326cca2ccf0715595595e2ac8f24cd0000003302de&sl=73465934&expires=8h&rt=sh&r=684010141&mlogid=6277480452656801297&vuk=303322248&vbdid=839227008&fin=%E7%BD%97%E5%A4%A7%E4%BD%91+-+%E4%BD%A0%E7%9A%84%E6%A0%B7%E5%AD%90+-+%E9%98%BF%E9%83%8E%E7%9A%84%E6%95%85%E4%BA%8B+%E4%B8%BB%E9%A2%98%E6%9B%B2.mp3&fn=%E7%BD%97%E5%A4%A7%E4%BD%91+-+%E4%BD%A0%E7%9A%84%E6%A0%B7%E5%AD%90+-+%E9%98%BF%E9%83%8E%E7%9A%84%E6%95%85%E4%BA%8B+%E4%B8%BB%E9%A2%98%E6%9B%B2.mp3&rtype=1&iv=0&dp-logid=6277480452656801297&dp-callid=0.1.1&hps=1&tsl=190&csl=190&csign=HoNbgOZNuKg%2F5UYsOrDCrMWzhG0%3D&so=0&ut=6&uter=4&serv=0&uc=1497965227&ic=3686759200&ti=9e71610225521574e561b9e80fb5a8af078c0a2024e73bfa&by=themis"
    downloadUrl = "http://m7.music.126.net/20170928182531/e72393e2febb9ffe5e5c0aa37015066c/ymusic/3c53/0591/6678/daef2ead5d613eb8e63b49f8e6dda6e4.mp3"


    opener = urllib.request.build_opener()
    with opener.open(fullurl=downloadUrl, data=None) as music:
        with open(musicFile, "wb") as musicFile:
            musicFile.write(music.read())

    print("下载音乐完毕")