import requests
from bs4 import BeautifulSoup
import datetime,time

def check_status(userName):
	result = requests.get("http://tw.op.gg/summoner/userName="+userName)
	soup = BeautifulSoup(result.text,'html.parser')
	rank = (soup.select(".tierRank")[0].string)
	deadline = datetime.date(2018,5,31)
	now = time.localtime()
	count = datetime.date(now[0], now[1], now[2])


	response = {'summoner_name':userName,'currentRank':rank,'currentTime':"5月"+str((count-deadline).days+31)+"日","message":"仲未上金" if("Silver" in rank or "Brozen" in rank) else "終於上左" }
	return response
#tierRank

res = check_status("Username")
print(res)
