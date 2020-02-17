import re
import requests
from bs4 import BeautifulSoup
import traceback
from datetime import datetime, timedelta

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def get_link_list():
    '''return url list of all funds'''
    fund_list_url = 'http://fund.eastmoney.com/allfund.html'
    text = get_html(fund_list_url)
    fund_url_list = re.findall(r'http://fund.eastmoney.com/\d{6}.html', text)
    return fund_url_list


def get_fund_info(fund_url):
    '''receive fund url, return a fund info dict'''
    fund_info = {}
    fund_info['id'] = re.findall(r'\d{6}', fund_url)[0]

    text = get_html(fund_url)
    soup = BeautifulSoup(text, 'html.parser')

    fund_return_list = soup.find_all('span', attrs={'class':'ui-font-middle ui-color-red ui-num'})

    fund_return_dict = {}
    fund_return_dict['1month'] = fund_return_list[2].text
    fund_return_dict['3month'] = fund_return_list[3].text
    fund_return_dict['6month'] = fund_return_list[4].text
    fund_return_dict['1year'] = fund_return_list[5].text
    fund_return_dict['3year'] = fund_return_list[6].text
    fund_return_dict['since_est '] = fund_return_list[7].text
    fund_info['returns'] = fund_return_dict
    fund_info['name'] = soup.find('span', attrs={'class':'funCur-FundName'}).text

    fund_info_table = soup.select('.infoOfFund')[0].find('table').find_all('td')
    fund_info['type'] = fund_info_table[0].find('a').text
    fund_info['risk'] = re.findall(r'\S{1,2}风险', fund_info_table[0].text)[0]
    fund_info['scale'] = fund_info_table[1].text.split('：')[1].split('（')[0]

    fund_manager_name_l = fund_info_table[2].find_all('a')
    fund_manager_name_list = []
    fund_manager_url_list = []
    for fund_manager_name in fund_manager_name_l:
        fund_manager_name_list.append(fund_manager_name.text)
        fund_manager_url_list.append(fund_manager_name.attrs['href'])

    fund_info['manager_list'] = fund_manager_name_list
    fund_info['establish_date'] = fund_info_table[3].text.split('：')[1]
    fund_info['establish_length'] = int((datetime.now().date() - datetime.strptime(fund_info['establish_date'], '%Y-%m-%d').date()).days / 365)
    fund_info['company'] = fund_info_table[4].text.split('：')[1]

    fund_manager_url = fund_manager_url_list[0]
    text_manager = get_html(fund_manager_url)
    soup_manager = BeautifulSoup(text_manager, 'html.parser')
    manager_info_table = soup_manager.select('.space8')[1].next_sibling.find_all('td')

    fund_info['manager_start'] = manager_info_table[0].text
    # fund_info['manager_end'] = manager_info_table[1].text
    fund_info['manager_period'] = manager_info_table[3].text
    fund_info['manager_returns'] = manager_info_table[4].text

    return fund_info


def get_fund_star(fund_id):
    fund_star = {'3 years': '', '5 years': ''}
    return fund_star 


def get_manager_info(manager_name):
    manager_info = {}
    return manager_info


def write_fund_info(fund_info):
    return


def main():
    test_url = 'http://fund.eastmoney.com/002692.html'
    info = get_fund_info(test_url)
    print(info)
    # url_list = get_link_list()
    # for url in url_list:
    #     print(url)
        # get_fund_info(url)


main()