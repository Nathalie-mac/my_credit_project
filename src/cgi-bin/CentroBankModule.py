import lxml
from lxml import etree
def find_dollar_course():
    res = ""
    tree = etree.parse('daily_eng_utf8.xml')
    root = tree.getroot()
    for valute in root:
        a = valute.find('Name')
        if (a.text == 'US Dollar'):
            res = valute.find('VunitRate').text
            break
    return res

