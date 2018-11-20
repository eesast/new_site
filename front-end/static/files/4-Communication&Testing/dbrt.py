#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import queue
import time
import urllib.request as req
from bs4 import BeautifulSoup


def extract_info(url):  # 如果不熟悉的话建议不要改这个函数
    try:
        content = req.urlopen(url).read()
        soup = BeautifulSoup(content, 'lxml', from_encoding='utf-8')

        title = soup.find('span', attrs={'property': 'v:itemreviewed'}).get_text()
        rating = float(soup.find('strong').get_text())
        reco_content = soup.find('div', attrs={'class': 'recommendations-bd'})
        recommendations = [x.get('href')[:-18] for x in reco_content.find_all('a')]

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

    while not recommendations.empty() and len(movie_info) < 20:  # 不要设太大
        url = recommendations.get()
        info, reco = extract_info(url)

        if info is not None:
            movie_info.append(info)
            for new_url in reco:
                if new_url not in checked_urls:
                    recommendations.put(new_url)
                    checked_urls.append(new_url)

            print(len(movie_info), 'finished!')
            time.sleep(1)  # 不要设太小

    movie_info.sort(key=lambda x: x['rating'], reverse=True)
    with open('result.json', 'wt', encoding='utf-8') as f:  # 结果写到 result.json
        json.dump(movie_info, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    main()
