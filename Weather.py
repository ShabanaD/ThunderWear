import json
import requests

class Weather:

    def __init__(self, city, country):
        #asks user for city and country they are in (country b/c some cities are common)
        #self.inputCity = input("What city do you live in? ")
        #self.inputCountry = input("What country do you live in? ")
        self.inputCity = city
        self.inputCountry = country
        self.weatherDict = {"temp": 0, "cond":""}
        self.locatCode = ""

    #uses location name to get dataCode for it
    def getIndicoInfo(self):
        locat = requests.get("https://hackathon.pic.pelmorex.com/api/search/string?keyword="+self.inputCity+" "+self.inputCountry)
        locatData = locat.json()
        self.locatCode = locatData["dataCode"]

    #gets current temperature data from observations
    def getTemp(self):
        obs = requests.get("https://hackathon.pic.pelmorex.com/api/data/observation?locationcode="+self.locatCode)
        obsData = obs.json()
        tempValue = obsData["data"]["temp"]
        self.weatherDict["temp"] = tempValue

    #gets keyword descriptor about weather
    def getCond(self):
        obs = requests.get("https://hackathon.pic.pelmorex.com/api/data/observation?locationcode="+self.locatCode)
        obsData = obs.json()
        desc = obsData["data"]["icon"]
        try:
            icon = requests.get("https://hackathon.pic.pelmorex.com/api/icon?locale=en-CA&obs="+desc)
            iconData = icon.json()
            descData = iconData["text"]
        except Exception:
            pass

        if ("rain" in descData or "drizzle" in descData):
            condData = "rain"
        elif ("snow" in descData or "hail" in descData):
            condData = "snow"
        else:
            condData = "clear"
        
        self.weatherDict["cond"] = condData

    #returns dictionary storing temperature and weather condition for use in Outfit.py
    def getDict(self):
        self.getIndicoInfo()
        self.getTemp()
        self.getCond()
        return self.weatherDict

    # gets weather message to be included in email
    def getEmailMsg(self):
        emailMsg = requests.get("https://hackathon.pic.pelmorex.com/api/weather/date?locationcode=" + self.locatCode + "&locale=en-CA")
        msgData = emailMsg.json()
        weathMsg = msgData["speech"]
        return weathMsg
        


'''
DICTIONARY FORMAT (for Outfit.py)

temp in degrees
keyword,-rain, clear, snow
info = {"temp": #, "cond": string)
'''


'''
ICON CODES (for conditions)

1-
2- SCT a few clouds, -BKN variably cloudy, BN - blowing sand
3- BKN partly cloudy
4-
5-
6-
7-
8- OVC/OVCN overcast
9- L/LN drizzle
10-
11- A-/ A-N light hail
12-
13-
14-
15-
16- S-/S-N light snow
17-
18- CLRN clear
19- HN haze, SCTN a few clouds, -BKNN variably cloudy 
20- BKNN partly cloudy
21- -OVCN mainly cloudy
22-
23-
24-
25-
26-
27-
28- R-N/R- light rain
29- RN rain

'''
