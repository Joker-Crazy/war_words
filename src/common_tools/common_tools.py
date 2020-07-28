import urllib.request as req
import urllib.request
import dateparser
from datetime import datetime as dt
from os import path
from lxml import html
import json
import time

from common_tools.common_consts import *


def get_content_by_link(link):
    try:
        with req.urlopen(link) as rf:
            return rf.read().decode('utf8')
    except urllib.error.HTTPError as err:
        return str(err)
    except urllib.error.URLError as err:
        return 'urllib.error.URLError'


def read_colected_data(path_to_json):
    res_json = dict()
    if path.exists(path_to_json):
        with open(path_to_json) as jsf:
            res_json = json.load(jsf)
    return res_json


def write_collected_data(path_to_json, **kwargs):
    with open(path_to_json, 'w') as fp:
        json.dump(kwargs, fp, ensure_ascii=False, indent=2)


def collect_data_links(base_url):
    content = get_content_by_link(get_url)

    tree = html.fromstring(content)
    return {item.attrib['href'] for item in tree.xpath(document_link_locator)}


def collect_ukranian_defenders_losses(*args, **kwargs):
    content = get_content_by_link(WIKI_URL)
    tree = html.fromstring(content)
    links_list = {item.attrib['href'] for item in tree.xpath(LINK_LOCATOR)}

    black_dates = list()
    for item in links_list:
        content = get_content_by_link(WIKI + item)
        if content == 'HTTP Error 404: Not Found':
            break
        elif content == 'HTTP Error 403: Forbidden':
            time.sleep(WAIT_FORBIDEN)
            continue
        tree = html.fromstring(content)
        tmp_dates = tree.xpath(WIKI_UKR_DEFENDER_KILLED_DATE_LOCATOR)
        black_dates += [tmp.text[1:] for tmp in tmp_dates if len(tmp.text)==11]
    print(len(black_dates))

    # Save articles content to json file like database
    res_dict = {WIKI: black_dates}
    write_collected_data(WIKI_UKR_DEFENDER_KILLED_DATE_PATH, **res_dict)
    
    return res_dict


def clear_text(*args):
    res = [item.text for item in args if str(item.text).lower() != 'none']
    if res:
        return ' '.join(res)
    else:
        return ''

def collect_ukr_president_data(*args, **kwargs):
    ts = dt.now().timestamp()
    get_date = ts

    # Loop for collecting article links 
    readed_links = read_colected_data(UKR_PRESIDENT_LINKS_PATH)
    links = set(readed_links[UKR_PRESIDENT_BASE_URL]) if readed_links else set()
    flag = True
    page_counter = 1
    while flag:
        content = ''
        day = dt.utcfromtimestamp(get_date).strftime('%d')
        month = dt.utcfromtimestamp(get_date).strftime('%m')
        year = dt.utcfromtimestamp(get_date).strftime('%Y')
        get_url = UKR_PRESIDENT_BASE_URL + \
            NEWS_SELECTION_BY_PAGE_DATES.format(start_date='01-01-2000',
                                                end_date='-'.join([day,month,year]),
                                                page_number=page_counter)

        print(get_url)

        content = get_content_by_link(get_url)
        if content == 'HTTP Error 404: Not Found':
            break
        elif content == 'HTTP Error 403: Forbidden':
            time.sleep(WAIT_FORBIDEN)
            continue
        elif content == 'urllib.error.URLError':
            continue

        tree = html.fromstring(content)
        links_list = {item.attrib['href'].split(UKR_PRESIDENT_BASE_URL)[1] for item in tree.xpath(ARTICLE_LINK_LOCATOR)}
        if links_list.issubset(links) and len(links):
            break
        else:
            links = links.union(links_list)
        time.sleep(WAIT_GET * 10)
        page_counter += 1
        # flag = False

    # Save article links to json file. Json file used as database
    write_collected_data(
        UKR_PRESIDENT_LINKS_PATH,
        **{UKR_PRESIDENT_BASE_URL: list(links)}
    )

    # Loop for colecting article content
    res_dict = read_colected_data(UKR_PRESIDENT_CONTENT_PATH)

    for item in links - res_dict.keys():
        tmp = {}
        get_url = UKR_PRESIDENT_BASE_URL + item
        print(get_url)

        content = get_content_by_link(get_url)
        if content == 'HTTP Error 404: Not Found':
            break
        elif content == 'HTTP Error 403: Forbidden':
            time.sleep(WAIT_FORBIDEN)
            continue
        elif content == 'urllib.error.URLError':
            continue

        tree = html.fromstring(content)
        header = tree.xpath(ARTICLE_HEADER)
        date_value = tree.xpath(ARTICLE_DATE)
        content_value = tree.xpath(ARTICLE_CONTENT)

        tmp['header'] = header[0].text
        tmp['datetime'] = dateparser.parse(date_value[0].text).strftime('%Y-%m-%d %H:%M')
        tmp['content'] = clear_text(*content_value)
        res_dict[item] = tmp

        time.sleep(WAIT_GET * 10)

    print(len(links))

    # # Save articles content to json file like database
    write_collected_data(UKR_PRESIDENT_CONTENT_PATH, **res_dict)
    
    return res_dict

def collect_kremlin_data(*args, **kwargs):
    ts = dt.now().timestamp()
    get_date = ts

    # Loop for collecting article links 
    readed_links = read_colected_data(KREMLIN_LINKS_PATH)
    links = set(readed_links[KREMLIN_BASE_URL]) if readed_links else set()
    flag = True
    while flag:
        content = ''
        day = dt.utcfromtimestamp(get_date).strftime('%d')
        month = dt.utcfromtimestamp(get_date).strftime('%m')
        year = dt.utcfromtimestamp(get_date).strftime('%Y')
        get_url = KREMLIN_BASE_URL + BY_DATE_URL.format(day=day,
                                                        month=month,
                                                        year=year)

        print(get_url)

        content = get_content_by_link(get_url)
        if content == 'HTTP Error 404: Not Found':
            break
        elif content == 'HTTP Error 403: Forbidden':
            time.sleep(WAIT_FORBIDEN)
            continue

        tree = html.fromstring(content)
        links_list = {item.attrib['href'] for item in tree.xpath(DOCUMENT_LINK_LOCATOR)}
        if links_list.issubset(links) and len(links):
            break
        else:
            links = links.union(links_list)
        time.sleep(WAIT_GET)
        get_date -= DAY_SECONDS

    # Save article links to json file. Json file used as database
    write_collected_data(
        KREMLIN_LINKS_PATH,
        **{KREMLIN_BASE_URL: list(links)}
    )

    # Loop for colecting article content
    res_dict = read_colected_data(KREMLIN_CONTENT_PATH)

    for item in links - res_dict.keys():
        tmp = {}
        get_url = KREMLIN_BASE_URL + item
        print(get_url)

        content = get_content_by_link(get_url)
        if content == 'HTTP Error 404: Not Found':
            break
        elif content == 'HTTP Error 403: Forbidden':
            time.sleep(WAIT_FORBIDEN)
            continue

        tree = html.fromstring(content)
        header = tree.xpath(BASE_LOCATOR + HEADER_LOCATOR)
        date_value = tree.xpath(BASE_LOCATOR + DATE_LOCATOR)
        time_value = tree.xpath(BASE_LOCATOR + TIME_LOCATOR)
        content_summary = tree.xpath(BASE_LOCATOR + CONTENT_DESCRIPTION_LOCATOR)
        content_value = tree.xpath(BASE_LOCATOR + CONTENT_LOCATOR)

        tmp['header'] = header[0].text
        tmp['datetime'] = dateparser.parse(
            date_value[0].text + time_value[0].text
        ).strftime('%Y-%m-%d %H:%M')
        tmp['summary'] = clear_text(*content_summary)
        tmp['content'] = clear_text(*content_value)
        res_dict[item] = tmp

        time.sleep(WAIT_GET)

    print(len(links))

    # Save articles content to json file like database
    write_collected_data(KREMLIN_CONTENT_PATH, **res_dict)
    
    return res_dict
