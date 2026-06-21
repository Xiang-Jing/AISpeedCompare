# -*- coding: utf-8 -*-
from sikuli import *
import json
import os
import sys


PERIOD_IMAGES = {
    u"03": "yijixuanxiang.png",
    u"06": "zhongbaoxuanxiang.png",
    u"09": "sanjixuanxiang.png",
    u"12": "nianbaoxuanxiang.png",
}


def load_request():
    json_input = sys.argv[1] if len(sys.argv) > 1 else os.path.join(getBundlePath(), "input.json")
    if os.path.isfile(json_input):
        with open(json_input, "rb") as json_file:
            payload = json.load(json_file)
    else:
        payload = json.loads(json_input)

    if not isinstance(payload, dict):
        raise ValueError("request body must be a JSON object")

    output_file_name = unicode(payload.get("outputFileName", u"")).strip()
    if not output_file_name:
        raise ValueError("outputFileName is required")

    params = payload.get("params")
    if not isinstance(params, list) or not params:
        raise ValueError("params must be a non-empty list")

    cases = []
    for item in params:
        stock_code = unicode(item["stockCode"])
        report_date = unicode(item["reportDate"])
        if len(report_date) < 6 or report_date[4:6] not in PERIOD_IMAGES:
            raise ValueError("unsupported reportDate: %s" % report_date)
        cases.append((stock_code, report_date))
    return output_file_name, cases


def open_ede():
    wait("jianpanjingling.png", 10).click()
    type("a", Key.CTRL)
    paste("EDE")
    type(Key.ENTER)
    wait(5)


def enter_all_codes(cases):
    entered_codes = []
    for stock_code, report_date in cases:
        if stock_code in entered_codes:
            continue
        wait("shurudaima.png", 10).click()
        type("a", Key.CTRL)
        paste(stock_code)
        wait(1)
        type(Key.ENTER)
        wait(1)
        entered_codes.append(stock_code)
        print("code entered: %s" % stock_code)


def unique_report_dates(cases):
    report_dates = []
    for stock_code, report_date in cases:
        if report_date not in report_dates:
            report_dates.append(report_date)
    return report_dates


def select_indicator(report_date):
    year = report_date[:4]
    month = report_date[4:6]

    wait("searchbypinyin.png", 10).click()
    waitVanish("searchbypinyin.png", 5)
    paste(u"每股转增股本-内地股票指标-分红指标")
    type(Key.ENTER)
    wait("meiguzhuanzenggubenshuangji.png", 10).doubleClick()
    waitVanish("meiguzhuanzenggubenshuangji.png", 5)
    wait(Pattern("nianfenxuanze.png").targetOffset(-72,0), 10).click()
    type(year)
    type(Key.ENTER)
    wait(Pattern("jiduxuanze.png").exact(), 10).click()
    wait(0.8)
    wait(PERIOD_IMAGES[month], 10).click()
    wait(3)
    type(Key.ENTER)
    wait(1)
    print("indicator selected for reportDate: %s" % report_date)


App.focus(u"Wind金融终端..Alice")
wait(3)

output_file_name, cases = load_request()
open_ede()
enter_all_codes(cases)

for report_date in unique_report_dates(cases):
    select_indicator(report_date)

wait("tiqushuju.png", 10).click()
wait("daochushuju.png", 10).click()
waitVanish("daochushuju.png", 5)
wait(Pattern("quxiaoxiazaiwandakai.png").targetOffset(-25,0), 10).click()

wait(Pattern("daochuwenjianming.png").targetOffset(36,0), 10).click()
wait(0.3)

type("a", Key.CTRL)
wait(0.2)
type(Key.BACKSPACE)
wait(0.2)
paste(output_file_name)

wait("lijixiazai.png", 10).click()
