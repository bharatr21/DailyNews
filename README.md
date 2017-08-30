# DailyNews
## Trending news headlines fetcher
Runs on Python3 (v3.5 and above) on Ubuntu

Install File Dependencies for this program by running:-
```sh
sudo pip install -r requirements.txt
```
Before using this program,
Create a file named `apikeys.py` and get an API Key from [News Articles API](https://newsapi.org/account) after creating an account there and then in that file, enter
```python
apikey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
After which one can run the program (on Ubuntu) by:
```sh
sudo python3 DailyNews.py
```
### Known Bugs/Issues
Currently, the program is known to run slowly (takes atleast 5-6 min) which is due to single-threadedness.Multithreading will be added soon.

Powered by:[NewsAPI](https://newsapi.org)
