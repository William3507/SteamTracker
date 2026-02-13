'''
Created: 2025-02-13
Author: William Bailey

Description: Clean and clear way of getting different things from the steam api. 
This is where I will put all the functions that get data from the steam api, and then I can call them in 
the main file to get the data I need.

'''

import requests
import os
from dotenv import load_dotenv


#Get Global Achievement Stats for a game:
#Return Format: { "achievementpercentages": { "achievements": [ { "name": "ACHIEVEMENT_WIN_SCENARIO_01_IMMORTAL", "percent": 0.1234 }, ... ] } }
def getGlobalAchievementStats(gameID, formatType):
    url = 'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v002/?gameid=' + gameID + '&format=' + formatType

    response = requests.get(url)

    #Fail gracefully
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nUnable to connect for some reason.                       \nCheck obtain.py: getGlobalAchievementStats.    \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



'''
{'game': {'gameName': 'ValveTestApp8930', 'gameVersion': '109', 'availableGameStats': 
{'achievements': [
    {'name': 'ACHIEVEMENT_WIN_WASHINGTON', 
    'defaultvalue': 0, 
    'displayName': 'First in the Hearts of Your Countrymen', 
    'hidden': 0, 
    'description': 'Beat the game on any difficulty setting as Washington.', 
    'icon': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/8930/4cf17a59d70b2decfd4369de8a7429e7b00f5ab8.jpg', 
    'icongray': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/8930/2ce109f9be6cb3193a385444b9b0b0ffcc7b2219.jpg'},
'''
#Get Personal Achievement Stats for a game :
def getAchievementDisplayStats(gameID, steamKey):
    url = 'https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key='+ steamKey + '&appid=' + gameID
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nUnable to connect for some reason.                       \nCheck connectToSteam.py: getPersonalAchievementStats.    \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
