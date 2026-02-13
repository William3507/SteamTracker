'''
Created: 2025-02-13
Author: William Bailey

Description: Unfortunately, Steam's API is a bit annoying when it comes to giving out Achievement names. 
The Api provides the names of the achievements, but only in internal format only (ACHIEVEMENT_WIN_SCENARIO_01_IMMORtAL).
While not the end of the world, for readability, I'm going to try and make it the display name of the achievement (Gengis Khan).

'''

#Two json inputs I expect to receive:

# - GetAchievement Display Stats - 
# This has the display name and a large quantity of addiitonal inormation about general stat tracking. 
# getAchievementDisplayStats(gameID, steamKey):

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

# - Get Global Achievement Stats -
# This has the percentage of players that have achieved each achievement, but only in internal format.
# getGlobalAchievementStats(gameID, formatType):

'''
Return Format: { "achievementpercentages": 
                    { "achievements": [ 
                        { "name": "ACHIEVEMENT_WIN_SCENARIO_01_IMMORTAL", "percent": 0.1234 }, ... ] } }
'''




#1. Receieve two data sets,
#       a. make sure they exist in a format I am expecting
#2. Create new dataset that has display name, rarity, and description of each achievement.
#3. Return new dataset to main file for use in data analysis and visualization.




 

