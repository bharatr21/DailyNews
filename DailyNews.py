import requests as req
from requests.exceptions import ConnectionError as ce
from urllib3.exceptions import MaxRetryError,NewConnectionError
import asyncio
import concurrent.futures
import multiprocessing
from multiprocessing import Process
import os
import sys
import re
import bs4
from apikeys import apikey
import urllib
import urllib.request
from urllib.parse import urlencode
#import time
#t = time.process_time()
def printinfo(string):
	with open('DailyNews.log','a+') as f1:
		f1.write(string)
def Worker(arg):
	# elif(KeyboardInterrupt):
	#     sys.exit()
    with open(os.path.join(mypath,str(arg['source']))+".txt","w+") as f:
        f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        f.write(str(arg['source']).title()+'\n')
        f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        for k in range(len(arg['articles'])):
            f.write('-----------------------------------------------------\n')
            f.write(str(arg['articles'][k]['title'])+'\n')
            f.write('-----------------------------------------------------\n')
            f.write(str(arg['articles'][k]['description'])+'\n')
            f.write('-----------------------------------------------------\n')
            f.write('Author:-'+str(arg['articles'][k]['author'])+'\n')
            f.write('-----------------------------------------------------\n')
            if arg['articles'][k]['urlToImage'] is not None:
                try:
                    os.chdir(imgpath)
                except (OSError,WindowsError):
                    os.chdir(mypath)
                try:
                    c='Downloading images embedded in articles from {}'.format(arg['source'])
                    printinfo(c)
                    urllib.request.urlretrieve(arg['articles'][k]['urlToImage'],'{}-{}'.format(arg['source'],k+1))
                except:
                    d='No images found for the {}th {} article.'.format(k+1,arg['source'])
                    printinfo(d)
cwd = os.getcwd()
mypath = os.path.join(cwd,'DailyNews')
imgpath = os.path.join(mypath,'Images')
if not os.path.exists(mypath):
    os.makedirs(mypath)
if not os.path.exists(imgpath):
    os.makedirs(imgpath)
KEY = apikey
sites=['ars-technica','al-jazeera-english','bloomberg','bbc-news','bbc-sport','buzzfeed','cnn','engadget','espn','espn-cric-info','fortune','google-news','hacker-news','ign','mashable','mtv-news','national-geographic','new-york-magazine','new-scientist','reddit-r-all','reuters','techcrunch','techradar','the-hindu','the-economist','the-huffington-post','the-new-york-times','the-next-web','the-telegraph','the-times-of-india','the-wall-street-journal','the-washington-post','the-verge','time']
times = ['top','latest','popular']
url_list=[]
for i in range(len(sites)):
    for j in range(len(times)):
        payload={'source':sites[i],
                 'sortBy':times[j],
                 'apiKey':KEY
                };
        qstring=urlencode(payload)
        url='https://newsapi.org/v1/articles?'+qstring
        url_list.append(url)
r = []        
async def webreqsend():
	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as Executor:
		loop = asyncio.get_event_loop()
		try:
			futures = [loop.run_in_executor(Executor,req.get,u) for u in url_list]
		except (ce,MaxRetryError,TimeoutError,NewConnectionError) as e:
			printinfo(e)
		for responses in await asyncio.gather(*futures):
			r.append(responses)
loop = asyncio.get_event_loop()
loop.run_until_complete(webreqsend())
rsonlist=[]
for i in range(len(r)):
    if r is None:
    	x='Whole Object is None'
    	printinfo(x)
    elif r[i] is None:
        y='Particular object is None'
        printinfo(y)
    elif r[i] is not None:
        rso=r[i].json()
    elif rso['status']=='error':
        z='Response Error'
        printinfo(z)
    if r[i] is not None and rso['status']!='error':
        rsonlist.append(r[i].json())
k=len(rsonlist)
a='Requests completed'
printinfo(a)
p=[Process(target=Worker,args=(rsonlist[i],)) for i in range(k)]
for process in p:
	process.start()
for process in p:
	process.join() 
#elapsed_time = time.process_time()-t
#print("\nTime Taken: %ds\n"%(elapsed_time))