# DailyNews
## Trending news headlines fetcher
Runs on Python3 (v3.5 and above) on Ubuntu

Install File Dependencies for this program by running:-
```sh
sudo pip3 install -r requirements.txt
```
Before using this program,
Create a file named `apikeys.py` and get an API Key from [News Articles API](https://newsapi.org/register) after creating an account check [this link](https://newsapi.org/account) and then in the `apikeys.py` file, enter
```python
apikey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
After which one can run the program (on Ubuntu) by:
```sh
sudo python3 DailyNews.py
```
### Known Bugs/Issues
Currently, the program is known to run slowly (takes atleast 5-6 min) which is bound to occur on slow internet connections, the appropriate timeouts will be added soon, and if possible, multiprocessing (instead of multithreading) may be needed to optimize this program/script.

Powered by:[NewsAPI](https://newsapi.org)
