
import requests
import os
from dotenv import load_dotenv


'''
def connect_to_test():
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print(f"Unable to connect for some reason. \n ~~~~~~~~ \n Check connectToSteam.py line 7-11.")
        
    return 0

'''



def getGlobalAchievementStats(gameID, formatType):
    url = 'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v002/?gameid=' + gameID + '&format=' + formatType

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Unable to connect for some reason. \n ~~~~~~~~ \n Check connectToSteam.py: getGlobalAchievementStats.")


def getPersonalAchievementStats(steamKey, gameID):
    url = 'https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key='+ steamKey + '&appid=' + gameID
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nUnable to connect for some reason.                       \nCheck connectToSteam.py: getPersonalAchievementStats.    \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#stsStats = getGlobalAchievementStats('646570', 'json')

load_dotenv()
localStsStats = getPersonalAchievementStats(str(os.getenv("STEAM_KEY")), '8930')



if localStsStats is not None:
    print(localStsStats)


    