#! py27w
import os, time
from datetime import datetime
from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference('browser.download.dir', os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/vnd.ms-excel')
fp.set_preference("browser.download.dir", "c:\\tmp");
driver = webdriver.Firefox(firefox_profile=fp)
driver.get('https://www.zacks.com/earnings/earnings-reports')


def click_calendar():
    try:
        element_xpath = '//*[@id="earnings_release"]/div[1]/p/a'
        element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(element_xpath).click()
        )
    finally:
        print("clicked calendar")


def click_prev_day(x):
    s = 'datespan_%d' % (x)
    try:
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(s).click()
        )
    except:
        result = False
    else:
        result = True
    return result


def click_export():
    try:
        element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('export_excel').click()
        )
    except:
        result = False
    else:
        result = True
    return result


def click_prev_month():
    try:
        driver.find_element_by_id('prevCal').click()
    except:
        result = False
    else:
        result = True
    i = 31
    while i > 27:
        try:
            click_prev_day(i)
            return False
        except:
            print('could not find %s in prev month' % (i))
            i -= 1


def subtract_day(n):
    y = n - 1
    return y


def start_date():
    return datetime(2016, 2, 29)


def click_to_start_date():
    start_date = datetime(2016, 2, 28)
    a = date.today()
    b = start_date
    c = a.month - b.month
    if c > 0:
        click_calendar()
        while c > 0:
            click_prev_month()
            c -= 1
        try:
            click_prev_day(31)
        except:
            click_prev_day(30)


def main():
    # click_to_start_date()
    # sdate = start_date()
    m = 12
    while m > 0:
        m -= 1
        for x in range(31, 0, -1):
            click_calendar()
            click_prev_day(x)
            click_export()

        click_calendar()
        click_prev_month()


if __name__ == '__main__':
    main()
