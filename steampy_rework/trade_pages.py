import requests
import bs4
import sys
import string
import re
from bs4 import BeautifulSoup, Tag




def isInt(value):
    if int(value) == value:
        return True
    else:
        return False


def get_name_by_ids(ids_data, proxy):
    try:
        req = requests.get(f'https://steamcommunity.com/economy/itemclasshover/{ids_data}?content_only=1&l=english', proxies=proxy).text
        data_of_item = (req.split('BuildHover')[1])
        pattern_hash_name = r"\"market_hash_name\":\".+\",\"market_name\""
        hash_name = re.search(pattern_hash_name, data_of_item)
        hash_name = str(format(hash_name.group(0))).replace('","market_name"', '').replace('"market_hash_name":"', '')
    except:
        hash_name = f'Error while getting name item: {ids_data}'
    return hash_name


def check_item_to_you(item_to):
    if item_to == 0:
        return [True, 1]
    else:
        return [False, 0]


def get_steamuid(html):
    id_list = []
    dates = html.find_all("a", {"data-miniprofile": True})
    for data in dates:
        id_list.append(data.get('data-miniprofile'))
    return id_list


def get_sent_offers(page_html, proxy):
    item_to = 0
    trade_number = 0
    document = BeautifulSoup(page_html, "html.parser")
    data_offerids = document.findAll("div", {"class": "tradeoffer"})
    tradesID_list = list()
    trades_data = dict()
    items_trade = {}
    for id_trade in data_offerids:
        if 'class="tooltip_hint"' in str(id_trade):
            tradeofferid = id_trade.get('id')
            tradeofferid = int(str(tradeofferid).replace('tradeofferid_', ''))
            tradesID_list.append(tradeofferid)
            data = id_trade.findAll("div", {"class": "tradeoffer_item_list"})
            steamids = get_steamuid(id_trade)
            for i in data:
                #Each iter it's half of trade
                data_items = []
                data_2 = (i.find_all("div", {"class": "trade_item"}))
                for i2 in data_2:
                    item = i2.get('data-economy-item')
                    item = str(item).replace('classinfo/', '')
                    item_split = str(item).replace('classinfo/','').split('/')
                    if  len(item_split) == 3:
                        item = (get_name_by_ids(item, proxy))
                        data_items.append(item)
                    elif len(item_split) == 2:
                        item = (get_name_by_ids(f'{item}/0', proxy))
                        data_items.append(item)

                if isInt(trade_number):
                    tradeID = tradesID_list[int(trade_number)]
                    items_trade[tradeID] = {'items_to_give': data_items}
                    items_trade[tradeID]['steamid'] = steamids[1]
                else:
                    tradeID = tradesID_list[int(trade_number-0.5)]
                    items_trade[tradeID]['items_to_receive'] =  data_items
                trade_number += 0.5
    return items_trade



def get_recived_offers(page_html, proxy):
    item_to = 0
    trade_number = 0
    document = BeautifulSoup(page_html, "html.parser")
    data_offerids = document.findAll("div", {"class": "tradeoffer"})
    tradesID_list = list()
    trades_data = dict()
    items_trade = {}
    for id_trade in data_offerids:
        if '<div class="tradeoffer_items_ctn inactive">' not in str(id_trade):
            steamids = get_steamuid(id_trade)
            tradeofferid = id_trade.get('id')
            tradeofferid = int(str(tradeofferid).replace('tradeofferid_', ''))
            tradesID_list.append(tradeofferid)
            data = id_trade.findAll("div", {"class": "tradeoffer_item_list"})
            for i in data:
                #Each iter it's half of trade
                data_items = []
                data_2 = (i.find_all("div", {"class": "trade_item"}))
                for i2 in data_2:
                    item = i2.get('data-economy-item')
                    item = str(item).replace('classinfo/', '')
                    item_split = str(item).replace('classinfo/', '').split('/')
                    if len(item_split) == 3:
                        item = (get_name_by_ids(item, proxy))
                        data_items.append(item)
                    elif len(item_split) == 2:
                        item = (get_name_by_ids(f'{item}/0', proxy))
                        data_items.append(item)
                if isInt(trade_number):
                    tradeID = tradesID_list[int(trade_number)]
                    items_trade[tradeID] = {'items_to_receive': data_items}
                    items_trade[tradeID]['steamid']= steamids[0]
                else:
                    tradeID = tradesID_list[int(trade_number - 0.5)]
                    items_trade[tradeID]['items_to_give'] = data_items
                trade_number += 0.5
    return items_trade



