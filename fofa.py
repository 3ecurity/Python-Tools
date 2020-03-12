import re,sys,requests,base64,time
from bs4 import BeautifulSoup

headers = {'X-Requested-With': 'XMLHttpRequest',
           'Cookie': '_fofapro_ars_session='+sys.argv[3]}
def fofadown(page,search):
    #search = '''title="404 NOT FOUND" && body="Hypertext"'''
    for i in range(int(page)):
        url = "https://fofa.so/result?page="+str(i+1)+"&qbase64="+str(base64.b64encode(search.encode("utf-8")))[2:-1]
        print(url)
        time.sleep(3)
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.content,"lxml")
        strings = str(soup.find_all(class_='list_mod_t'))

        UrlMatches = []

        UrlRegex = re.compile(r'''(([A-Za-z]+://)([-\w]+(?:\.\w[-\w]*)+)(:\d+)?(/[^.!,?"<>\[\]{}\s\x7F-\xFF]*(?:[.!,?]+[^.!,?"<>\[\]{}\s\x7F-\xFF]+)*)?
        )''', re.VERBOSE)

        for UrlGroups in UrlRegex.findall(strings):
            UrlMatches.append(UrlGroups[0])

        NewFile = open(sys.argv[2],'a')
        UrlList = list(set(UrlMatches))
        UrlList_nums = len(UrlList)



        for line in range(UrlList_nums):
            if "\\n" in UrlList[line]:
                pass
            else:
                print(UrlList[line])
                NewFile.writelines(UrlList[line]+"\n")

        NewFile.close()

        print("\nSuccess\n")
fofadown(sys.argv[1],input("Search:"))
