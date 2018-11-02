#!/usr/bin/python
import json
import urllib.request
import sys
import getopt


def main(argv):
    trader = ''  
    kaufdatum = ''
    kaufwert = 0
    timestamp = []
    wert = []
    wertatdatum = 1
    try:
        opts, args = getopt.getopt(argv, "ht:d:w:", ["trader=", "datum=", "kaufwert"])
    except getopt.GetoptError:
        print('autohtml.py -t <trader name> -d <kaufdatum YYYY-MM-DD> -w <kaufwert>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('autohtml.py -t <trader name> -d <kaufdatum YYYY-MM-DD> -w <kaufwert>')
            sys.exit()
        elif opt in ("-t", "--trader"):
            trader = arg
        elif opt in ("-d", "--datum"):
            kaufdatum = arg
        elif opt in ("-w", "--kaufwert"):
            kaufwert = float(arg)

    with urllib.request.urlopen("https://www.etoro.com/sapi/userstats/CopySim/Username/"
                                + trader
                                + "/lasttwoyears") as url:
        data = json.loads(url.read().decode())

    for element in data['simulation']['lastTwoYears']['chart']:
        var = element.get('timestamp')
        if kaufdatum in var:
            wertatdatum = element.get('equity')
    for element in data['simulation']['lastTwoYears']['chart']:
        if wertatdatum == -1:
            print('kaufdatum ausserhalb des betrachteten Zeitraums')
        var = element.get('timestamp')
        timestamp.append(var[8:10] + '.' + var[5:7] + '.' + var[2:4])  # ii.get('timestamp')
        wert.append(element.get('equity') * kaufwert / wertatdatum)
    # print(timestamp)
    # write to html
    html = '<html xmlns="http://www.w3.org/1999/xhtml" lang="de">' \
           '<table>\n' \
           '<thead>\n' \
           '<tr>\n' \
           '<th>Datum</th>' \
           '<th>Close</th>' \
           '<th>Low</th>' \
           '<th>High</th>' \
           '</tr>\n' \
           '</thead>\n' \
           '<tbody>\n'

    for ii in range(len(timestamp)):
        html += '<tr>\n<td>' + timestamp[len(timestamp)-ii-1] + '</td>' \
                '<td>' + str(wert[len(timestamp)-ii-1]).replace('.', ',') + '</td>' \
                '<td>' + str(wert[len(timestamp)-ii-1]).replace('.', ',') + '</td>' \
                '<td>' + str(wert[len(timestamp)-ii-1]).replace('.', ',') + '</td>' \
                '</tr>\n'
    html += '</tbody>\n</table>\n</html>\n'

    file_ = open('//NETDS/web/test/' + trader + '.html', 'w')
    file_.write(html)
    file_.close()


if __name__ == "__main__":
    main(sys.argv[1:])
