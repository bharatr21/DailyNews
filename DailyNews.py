import requests as req
import grequests
import threading
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
class FetcherThread(threading.Thread):
	def __init__(self,arg=None):
		threading.Thread.__init__(self)
		self.arg = arg
	def run(self):
		# elif(KeyboardInterrupt):
		#     sys.exit()
            with open(os.path.join(mypath,str(self.arg['source']))+".txt","w+") as f:
                f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                f.write(str(self.arg['source']).title()+'\n')
                f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                for k in range(len(self.arg['articles'])):
                    f.write('-----------------------------------------------------\n')
                    f.write(str(self.arg['articles'][k]['title'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    f.write(str(self.arg['articles'][k]['description'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    f.write('Author:-'+str(self.arg['articles'][k]['author'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    if self.arg['articles'][k]['urlToImage'] is not None:
                        try:
                            os.chdir(imgpath)
                        except (OSError,WindowsError):
                            os.chdir(mypath)
                        try:
                            print('Downloading images embedded in articles from {}'.format(self.arg['source']))
                            urllib.request.urlretrieve(self.arg['articles'][k]['urlToImage'],'{}-{}'.format(self.arg['source'],k+1))
                        except:
                            print('No images found for the {}th {} article.'.format(k+1,self.arg['source']))
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
responses = [grequests.get(u) for u in url_list]
r = grequests.map(responses)
rsonlist=[]
for i in range(len(r)):
    if r is None:
        pass
    elif r[i] is None:
        pass    
    elif r[i] is not None:    
        rso=r[i].json()        
    elif rso['status']=='error':
        pass
    elif r[i] is not None:
        rsonlist.append(r[i].json())
k=len(rsonlist)		
# for i in range(k):
# 	print(rsonlist[i]['source'])			
t=[FetcherThread(rsonlist[i]) for i in range(k)]
for th in t:
	th.run()
for th in t:
    th.join()
#elapsed_time = time.process_time()-t
#print("\nTime Taken: %ds\n"%(elapsed_time))