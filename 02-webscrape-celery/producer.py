import time
from celery import Celery
import consumer

app = Celery('tasks', broker='amqp://localhost//')

def produce():
    with open(f'urls.txt', 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        consumer.download_url.delay(url)
        print(f"* Submitted: [{url}]")

produce()

#####################

#   urls.txt    #  example

"""
http://www.apple.com
http://www.amazon.com
http://www.abc.xyz
http://www.microsoft.com
http://www.facebook.com
http://www.alibabagroup.com
http://www.tencent.com
http://www.berkshirehathaway.com
http://www.jpmorganchase.com
http://www.exxonmobil.com
http://www.jnj.com
http://usa.visa.com
http://www.shell.com
http://www.samsung.com
http://www.bankofamerica.com
http://www.icbc.com.cn
http://www.wellsfargo.com
http://corporate.walmart.com
http://www.nestle.com
http://www.unitedhealthgroup.com
http://www.intel.com
http://www.att.com
http://www.chevron.com
http://www.ccb.com
http://www.homedepot.com
http://www.pfizer.com
http://www.verizon.com
http://www.toyota.co.jp
http://www.ab-inbev.com
http://www.mastercard.com
"""
