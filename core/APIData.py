import requests

headers = {"Client-ID": "do9riuwpoytsel2umu1nqq1zcaquc4", "Authorization": "Bearer wso04w82mg6m6varfnozbwrn8hdtl0"}
url = "https://api.twitch.tv/helix/"


def extraction(choice, username):
    options = {
        "User ID": getid,
        "User Details": getUserDetails,
        # "Game Details": getGameDetails,
        "Follower count": getFollowerCount,
        "User follows": getUserFollows,
        "Followers": getFollowers,
        "Video Clip Details": getVideoClipDetails,
        "Channel information": getChannelInfo,
        "Channel teams": getChannelTeams,
        "User chat color": getUserChatColor,
        "User chat settings": getUserChatSettings,
        # "User extensions": getUserExtensions,
    }
    return options[choice](username)


def getid(username):
    user_url = url + "users?login=" + username
    response = requests.get(user_url, headers=headers).json()
    data = str(response['data'][0]['id'])
    return data


# API DATA

def getUserDetails(username):  # prints data of specific user
    user_url = url + "users?login=" + username
    response = requests.get(user_url, headers=headers).json()
    data = response["data"][0]
    result = ""
    for i in data:
        result += str(i) + " : " + str(data[i]) + '\n'

    return result


# def getGameDetails(game):  # prints data of specific game
#     game_url = url + "games?name=" + game
#     response = requests.get(game_url, headers=headers).json()
#     return response["data"][0]


def getFollowerCount(channel):  # prints number of followers of a specific account
    channel_url = url + "channels/followers?broadcaster_id=" + getid(channel)
    response = requests.get(channel_url, headers=headers).json()
    data = response["total"]
    return "Total Followers: " + str(data)


def getUserFollows(username):  # prints details of all followed accounts of a specific user
    follows_url = url + "users/follows?from_id=" + getid(username)
    response = requests.get(follows_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getFollowers(username):  # prints details of all followers of a specific user
    follower_url = url + "users/follows?to_id=" + getid(username)
    response = requests.get(follower_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getVideoClipDetails(username):  # prints details of video clips of a specific user
    video_url = url + "clips?broadcaster_id=" + getid(username)
    response = requests.get(video_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getChannelInfo(channel):  # prints channel data
    info_url = url + "channels?broadcaster_id=" + getid(channel)
    response = requests.get(info_url, headers=headers).json()
    data = response["data"][0]
    result = ""
    for i in data:
        result += str(i) + " : " + str(data[i]) + '\n'
    return result


def getChannelTeams(channel):  # returns channel team name and team id if exists
    team_url = url + "teams/channel?broadcaster_id=" + getid(channel)
    response = requests.get(team_url, headers=headers).json()
    try:
        data = (response["data"][0]["team_name"], response["data"][0]["id"])
    except TypeError:
        return "No team"

    result = ""
    for i in data:
        result += str(i) + '\n'

    return result


def getUserChatColor(channel):  # prints color code chosen for username in chat
    color_url = url + "chat/color?user_id=" + getid(channel)
    response = requests.get(color_url, headers=headers).json()
    data = response["data"][0]["color"]

    if len(data) != 0:
        return "Color code chosen: " + data

    else:
        return "No chosen color"


def getUserChatSettings(username):  # prints details of chat settings of a specific user
    chat_settings_url = url + "chat/settings?broadcaster_id=" + getid(username)
    response = requests.get(chat_settings_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getUserExtensions(username):  # prints details of installed extensions of a specific user
    extensions_url = url + "users/extensions?user_id=" + getid(username)
    response = requests.get(extensions_url, headers=headers).json()
    data = response["data"]["panel"]
    result = ""
    for key in data:
        result += str(data[key]) + '\n'
    return result

