import hashlib
import io
import json
import logging
import operator
import random
import re
import datetime
import os
import socket
import time

import pandas as pd
import requests
import csv
import xlrd
import inspect
import ctypes
import pyaudio
from threading import Thread


def async_utils(f):
    '''
    异步装饰器
    '''

    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def write_csv(name, data_list):
    fieldnames = data_list[0]
    print(fieldnames)
    with open(name + '.csv', mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)


def data_to_json(data, name):
    with io.open(name + '.json', 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(data, ensure_ascii=False, indent=2, separators=(',', ': ')))


def pwd_hash(string):
    """password hash"""
    x = hashlib.sha256()
    salt = ''
    x.update((string + salt).encode())
    return x.hexdigest()


def set_random_string(length):
    """生成随机数"""
    ret = ''
    for i in range(length):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter_str = 'abcdefghjkmnpqrstuvwxyz'
        LETTER_STR = 'ABCDEFGHJKMNPQRSTUVWXYZ'
        letter = letter_str[random.randint(0, len(letter_str) - 1)]
        LETTER = LETTER_STR[random.randint(0, len(letter_str) - 1)]
        s = str(random.choice([num, letter, LETTER]))
        ret += s
    return ret


def json_to_csv(name):
    with open(name) as f:
        a = json.loads(f.read())
        write_csv(name, a)


def sort_dict(data, field):
    """
    sort dict
    :param data: [dict] the data to sort
    :param field: the field to sort
    :return:
    """
    for key, value in data.items():
        data[key] = sorted(value, key=operator.itemgetter(field))
    return data


def parse_price(num_str):
    """
    parse price
    :param num_str: [string] string of price
    :return: [float] num of price
    """
    try:
        result = re.search('(\d+\.*\d*)(.*)', num_str)
        num = float(result[1])
        unit = result[2]
        if re.search('万', unit):
            num *= 10000
        if re.search('千', unit):
            num *= 1000
        if re.search('百', unit):
            num *= 1000
        if re.search('亿', unit):
            num *= 100000000
        return num
    except Exception as e:
        print(e)
        return num_str


def get_img(url, path, name=None):
    if not name:
        name = url.split('/')[-1]
    path = os.path.join(path, name)
    res = requests.get(url)
    with open(path, 'wb') as f:
        f.write(res.content)
    return path


class GetProxy(object):
    def __init__(self):
        self.proxy_url = 'http://api.ip.data5u.com/dynamic/get.html?order=c77bcb61b876d0efe082d749462f13a7&json=1&sep=3'

    def get_proxy(self):
        res = requests.get(self.proxy_url)
        proxy_data = json.loads(res.text)
        if proxy_data['msg'] == 'ok':
            proxy_dict = proxy_data['data'][0]
            proxy = proxy_dict['ip'] + ':' + str(proxy_dict['port'])
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            res = requests.get('https://www.baidu.com', proxies=proxies)
            print(res.status_code)
            if res.status_code == 200:
                return proxies


def get_proxy():
    proxy = GetProxy()
    return proxy.get_proxy()


def data_to_csv(data_list, csv_key, name):
    """
    save data to csv
    :param data_list: data
    :param csv_key: csv column
    :param name: file name
    :return:
    """
    final_data = []
    for data in data_list:
        sign_key = []
        for key, value in data.items():
            sign_key.append(value)
        final_data.append(sign_key)
    # 将总数据转化为data frame再输出
    df = pd.DataFrame(data=final_data,
                      columns=csv_key)
    df.to_csv(name + '.csv', index=False, encoding='utf-8_sig')


def table_to_dict(browser):
    result = {}
    for row in browser.find_elements_by_xpath('//table//tr'):
        columns = row.find_elements_by_xpath('td')
        if len(columns) < 2:
            continue
        key = columns[0].text
        value = columns[1].text
        result[key] = value
    return result


def killport(port):
    """
    按端口号杀进程
    :param port:
    :return:
    """
    # 查找端口的pid
    find_port = 'netstat -aon | findstr %s' % str(port)
    result = os.popen(find_port)
    text = result.read()
    pid = text.strip().split(' ')[-1]
    # 占用端口的pid
    find_kill = 'taskkill -f -pid %s' % pid
    print(find_kill)
    result = os.popen(find_kill)
    return result.read()


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    '''
    系统停止线程
    '''
    _async_raise(thread.ident, SystemExit)


def port_is_used(port, ip='127.0.0.1'):
    '''
    检查端口是否占用
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        print('%s:%d is used' % (ip, port))
        return True
    except:
        print('%s:%d is unused' % (ip, port))
        return False


def get_device():
    '''
    获取当前音频设备
    '''
    device_list = []
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        devInfo = p.get_device_info_by_index(i)
        if devInfo['maxInputChannels'] == 0 or devInfo['hostApi'] != 0:
            continue
        device_list.append({'index': i, 'name': devInfo['name']})
    return sorted(device_list, key=lambda e: e.__getitem__('index'))


if __name__ == '__main__':
    # d = [{'date': '2019-06-01', 'ht': '25', 'lt': '12', 'weather': '多云', 'wind_dir': '西南风', 'wind_value': '5级'},
    #      {'date': '2019-06-27', 'ht': '28', 'lt': '16', 'weather': '多云', 'wind_dir': '西南风', 'wind_value': '4级'},
    #      {'date': '2019-06-28', 'ht': '26', 'lt': '13', 'weather': '多云', 'wind_dir': '西北风', 'wind_value': '5级'},
    #      {'date': '2019-06-29', 'ht': '20', 'lt': '11', 'weather': '阴', 'wind_dir': '东北风', 'wind_value': '2级'},
    #      {'date': '2019-06-30', 'ht': '23', 'lt': '13', 'weather': '晴', 'wind_dir': '东北风', 'wind_value': '2级'}]
    # write_csv('a', d)
    from log.log import create_log_decorator


    @create_log_decorator('test')
    def test(a, b, o):
        print(a + b)
        print(o)
        print('test')
        time.sleep(3)


    test(1, 2, {'t': 'test'})
