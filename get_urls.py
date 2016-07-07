# coding utf-8 
import urllib2
import get_data

count = 0
while count < 10:
    count = count + 1

    # Query for IT in Osaka only the first page
    url = "https://www.hellowork.go.jp/servicef/130050.do?kyushokuNumber1=&kyushokuNumber2=&kyushokuUmu=2&jigyoshomei=&kiboSangyo1=&kiboSangyo2=&kiboSangyo3=&chiku1=&ensen1_1=&ensen1_2=&chiku2=&ensen2_1=&ensen2_2=&chiku3=&kiboShokushu1=10&kiboShokushu2=&kiboShokushu3=&nenrei=&license1=&license2=&license3=&gekkyuKagen=&teate=1&shukyuFutsuka=0&nenkanKyujitsu=&rdoJkgi=9&shugyoJikanKaishiHH=&shugyoJikanKaishiMM=&shugyoJikanShuryoHH=&shugyoJikanShuryoMM=&freeWordType=0&freeWord=&freeWordRuigigo=1&notFreeWord=&commonSearch=%E6%A4%9C%E7%B4%A2&fwListNowPage=1&fwListLeftPage=1&fwListNaviCount=11&kyujinShuruiHidden=1&todofukenHidden=27&todofukenHidden=28&todofukenHidden=59&kyushokuUmuHidden=2&kiboShokushu1Hidden=10&teateHidden=1&shukyuFutsukaHidden=0&rdoJkgiHidden=9&freeWordRuigigoHidden=1&freeWordTypeHidden=0&actionFlgHidden=1&nowPageNumberHidden=1&screenId=130050&action=&codeAssistType=&codeAssistKind=&codeAssistCode=&codeAssistItemCode=&codeAssistItemName=&codeAssistDivide=&codeAssistRankLimit=&xab_vrbs=commonNextScreen%2CdetailJokenChangeButton%2CcommonDetailInfo%2CcommonSearch%2CcommonDelete"

    # Query for IT for Osaka
    url = "https://www.hellowork.go.jp/servicef/130050.do?fwListNaviBtn1="+`count`+"&fwListNowPage="+`count`+"&fwListLeftPage="+`count`+"&kyushokuNumber1=&kyushokuNumber2=&kyushokuUmu=2&jigyoshomei=&kiboSangyo1=&kiboSangyo2=&kiboSangyo3=&chiku1=&ensen1_1=&ensen1_2=&chiku2=&ensen2_1=&ensen2_2=&chiku3=&kiboShokushu1=10&kiboShokushu2=&kiboShokushu3=&nenrei=&license1=&license2=&license3=&gekkyuKagen=&teate=1&shukyuFutsuka=0&nenkanKyujitsu=&rdoJkgi=9&shugyoJikanKaishiHH=&shugyoJikanKaishiMM=&shugyoJikanShuryoHH=&shugyoJikanShuryoMM=&freeWordType=0&freeWord=&freeWordRuigigo=1&notFreeWord=&fwListNaviCount=11&kyujinShuruiHidden=1&todofukenHidden=27&todofukenHidden=28&todofukenHidden=59&kyushokuUmuHidden=2&kiboShokushu1Hidden=10&teateHidden=1&shukyuFutsukaHidden=0&rdoJkgiHidden=9&freeWordRuigigoHidden=1&freeWordTypeHidden=0&actionFlgHidden=1&nowPageNumberHidden=5&screenId=130050&action=&codeAssistType=&codeAssistKind=&codeAssistCode=&codeAssistItemCode=&codeAssistItemName=&codeAssistDivide=&codeAssistRankLimit=&xab_vrbs=commonNextScreen%2CdetailJokenChangeButton%2CcommonDetailInfo%2CcommonSearch%2CcommonDelete"

    print count
    
    response = urllib2.urlopen(url)
    html = response.read()

    table = get_data.get_table(html)
    get_data.get_rows(table)
