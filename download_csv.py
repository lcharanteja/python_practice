__author__ = 'charan'

from urllib import request

yahoo_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=11&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r"yahoo.csv"
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(yahoo_url)