import requests

headers = {"Client-ID": "aa00f8e0g4gic1bkruejtn1qvht9v3", "Authorization": "Bearer fd253rukwe5shngahs4eb1bzxlz7e8"}
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
