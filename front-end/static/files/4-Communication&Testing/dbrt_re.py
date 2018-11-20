#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 额外说明：这个文件是去除了 BeautifulSoup 的版本，不确定是否避免了 utf-8 编码问题
# 因此请在 BeautifulSoup 安装失败的情况下使用


import json
import queue
import re
import time
import urllib.request as req
from html.parser import HTMLParser


def extract_info(url):  # 如果不熟悉的话建议不要改这个函数
    try:
        content = req.urlopen(url).read().decode('utf-8', 'ignore')

        title = re.findall(r'<span property="v:itemreviewed">(.*?)</span>', content)[0]
        rating = float(re.findall(r'<strong class="ll rating_num" property="v:average">(.*?)</strong>', content)[0])
        reco = re.findall(r'/(\d*)/\?from=subject-page', content)
        recommendations = ['https://movie.douban.com/subject/%s/' % x for x in reco]

        return {'title': title, 'rating': rating, 'url': url}, recommendations

    except Exception as err:
        print(url, str(err))
        return None, None


def main():
    start_url = 'https://movie.douban.com/subject/20495792/'  # 请自行修改
    checked_urls = [start_url]
    movie_info = []
    recommendations = queue.Queue()
    recommendations.put(start_url)

    while not recommendations.empty() and len(movie_info) < 50:  # 不要设太大
        url = recommendations.get()
        info, reco = extract_info(url)

        if info is not None:
            movie_info.append(info)
            for new_url in reco:
                if new_url not in checked_urls:
                    recommendations.put(new_url)
                    checked_urls.append(new_url)

            print(len(movie_info), 'finished!')
            time.sleep(0.5)  # 不要设太小

    movie_info.sort(key=lambda x: x['rating'], reverse=True)
    with open('result.json', 'wt', encoding='utf-8') as f:  # 结果写到 result.json
        json.dump(movie_info, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    main()
