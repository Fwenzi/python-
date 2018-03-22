import requests
from http.cookies import SimpleCookie
from bs4 import BeautifulSoup


# 自定义headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36', 
    'Referer': 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html',
    'Host': 'sdcsts.jrj.com.cn:8080',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive'
}


# 将复制到cookies 转换为字典，方便调用
raw_cookies = ''
cookie = SimpleCookie(raw_cookies)
cookies = {i.key: i.value for i in cookie.values()}


# 尝试使用面向对象的方式来造爬虫
class Alipay_Bill_Info(object):
    '''支付宝账单信息'''
    def __init__(self, headers):
        '''
        类的初始化

        headers：请求头
        cookies: 持久化访问
        info_list: 存储账单信息的列表
        '''
        self.headers = headers
        # self.cookies = cookies
        # 利用requests库构造持久化请求
        self.session = requests.Session()
        # 将请求头和cookies添加到缓存之中
        self.session.headers = self.headers
        # self.session.cookies.update(self.cookies)
        self.info_list = []

    def login_status(self):
        '''判断登录状态'''
        status = self.session.get(
            'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html', timeout=5, allow_redirects=False).status_code
        print(status)
        if status == 200:
            return True
        else:
            return False

    def get_data(self):
        '''
        利用bs4库解析html
        并抓取数据，
        数据以字典格式保存在列表里
        '''
        status = self.login_status()
        url = 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html'
        if status:
            html = self.session.get(url).text
            soup = BeautifulSoup(html, 'lxml')
            print(soup.prettify())
            # 抓取前五个交易记录
            # trades = soup.find_all('tr', class_='J-item ')[:3]

            # for trade in trades:
            #     # 做一个try except 避免异常中断
            #     try:
            #         # 分别找到账单的 时间 金额 以及流水号
            #         time = trade.find('p', class_='text-muted').text.strip()
            #         amount = trade.find(
            #             'span', class_='amount-pay').text.strip()
            #         code = trade.find(
            #             'a', class_='J-tradeNo-copy J-tradeNo')['title']
            #         self.info_list.append(
            #             dict(time=time, amount=amount, code=code))
            #     except:
            #         self.info_list.append({'error': '出现错误,1'})

        else:
            self.info_list.append({'error': '出现错误,2'})


test = Alipay_Bill_Info(HEADERS)
test.get_data()

print(test.info_list)