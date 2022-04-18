import requests
from bs4 import BeautifulSoup
import  datetime
import  time
## get the url to find the content of data
now = datetime.datetime.now()
def get_hacker_new():

    url='https://news.ycombinator.com/news?p=2'
    cnt =''
    cnt+=('<b>Hacker new top stories:</b> \n'+'<br>'+'-'*50+'<br>'+"\n")
    request=requests.get(url).text
    soup=BeautifulSoup(request,'html.parser')
    all_links = soup.find_all('a',attrs={'class':'titlelink'})  # this will return all links+text
    for index,link in enumerate(all_links):
        if 'More' not in link.get_text():
            cnt+=(str(index+1)+' :: '+link.get_text()+"\n"+link.get('href')+"\n"+'<br>')
    print(cnt)
    with open(f'{now}.txt','w') as f:
     f.write(cnt)
     print(f'write to file')


'''print(cnt)
with open(f'{now}.txt','w') as f:
    str=repr(cnt)
    f.write(str+"\n")
    print(f'write to file')'''

## execute the code
if __name__=='__main__':
    while True:
         wait_time=500
         print(f'start the program- {now}')
         get_hacker_new()
         print(f'end of program -{now}')
         time.sleep(wait_time)








