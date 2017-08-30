import requests as req
import os
import sys
import re
import bs4
from apikeys import apikey
import urllib
import urllib.request
#import time
#t = time.process_time()
cwd = os.getcwd()
mypath = os.path.join(cwd,'DailyNews')
imgpath = os.path.join(mypath,'Images')
if not os.path.exists(mypath):
    os.makedirs(mypath)
if not os.path.exists(imgpath):
    os.makedirs(imgpath)
KEY = apikey
sites=['ars-technica','bbc-news','engadget','espn','espn-cric-info','google-news','ign','national-geographic','new-york-magazine','reddit-r-all','techcrunch','the-hindu','the-economist','the-new-york-times','the-times-of-india','the-wall-street-journal','the-washington-post','the-verge']
times = ['top','latest','popular']
for i in range(len(sites)):
    for j in range(len(times)):
        payload={'source':sites[i],
                 'sortBy':times[j],
                 'apiKey':KEY
                };
        try:
            r = req.get('https://newsapi.org/v1/articles',params=payload)
            rso = r.json()
            if(rso['status']=='error'):
                pass
            # elif(KeyboardInterrupt):
            #     sys.exit()
            else:
                rson = r.json()
                f = open(os.path.join(mypath,str(rson['source']))+".txt","w+")
                f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                f.write(str(rson['source']).title()+'\n')
                f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                for k in range(len(rson['articles'])):
                    f.write('-----------------------------------------------------\n')
                    f.write(str(rson['articles'][k]['title'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    f.write(str(rson['articles'][k]['description'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    f.write('Author:-'+str(rson['articles'][k]['author'])+'\n')
                    f.write('-----------------------------------------------------\n')
                    if rson['articles'][k]['urlToImage'] is not None:
                        try:
                        	os.chdir(imgpath)
                        except (OSError,WindowsError):
                        	os.chdir(mypath)
                        try:
                            urllib.request.urlretrieve(rson['articles'][k]['urlToImage'],'{}-{}'.format(rson['source'],k+1))
                        except:
	                        print('No images found for the {}th {} article.'.format(k+1,rson['source']))
                f.close()
        except(req.exceptions.SSLError,req.packages.urllib3.exceptions.SSLError,req.exceptions.ConnectionError):
            print('Connection Failed.')
        except(UnicodeEncodeError):
            print('Character Encoding Failed.')
#elapsed_time = time.process_time()-t
#print("\nTime Taken: %ds\n"%(elapsed_time))