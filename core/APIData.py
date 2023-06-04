import requests

headers = {"Client-ID": "aa00f8e0g4gic1bkruejtn1qvht9v3", "Authorization": "Bearer fd253rukwe5shngahs4eb1bzxlz7e8"}
url = "https://api.twitch.tv/helix/"


def getid(username):
    user_url = url + "users?login=" + username
    response = requests.get(user_url, headers=headers).json()
    result = response['data'][0]['id']
    return result


# API DATA

def getUserDetails(username):  # prints data of specific user
    user_url = url + "users?login=" + username
    response = requests.get(user_url, headers=headers).json()
    return response["data"][0]


def getTop20Games():  # prints data of top 20 broadcasted games
    topgames_url = url + "games/top"
    response = requests.get(topgames_url, headers=headers).json()
    return response["data"]


def getGameDetails(game):  # prints data of specific game
    game_url = url + "games?name=" + game
    response = requests.get(game_url, headers=headers).json()
    return response["data"][0]


def getGlobalEmotes():  # prints data of all global emotes that are used in chat
    emote_url = url + "chat/emotes/global"
    response = requests.get(emote_url, headers=headers).json()
    return response["data"]


def getTop20Streams():  # prints top 20 current streams
    stream_url = url + "streams"
    response = requests.get(stream_url, headers=headers).json()
    return response["data"]


def getTop20SoundtrackPlaylists():  # prints top 20 Soundtrack Playlists
    music_url = url + "soundtrack/playlists"
    response = requests.get(music_url, headers=headers).json()
    return response["data"]


def getFollowerCount(channel):  # prints number of followers of a specific account
    channel_url = url + "channels/followers?broadcaster_id=" + getid(channel)
    response = requests.get(channel_url, headers=headers).json()
    print(response["total"])


def getUserFollows(username):  # prints details of all followed accounts of a specific user
    follows_url = url + "users/follows?from_id=" + getid(username)
    response = requests.get(follows_url, headers=headers).json()
    return response["data"]


def getFollowers(username):  # prints details of all followers of a specific user
    follower_url = url + "users/follows?to_id=" + getid(username)
    response = requests.get(follower_url, headers=headers).json()
    return response["data"]


def getVideoClipDetails(username):  # prints details of video clips of a specific user
    video_url = url + "clips?broadcaster_id=" + getid(username)
    response = requests.get(video_url, headers=headers).json()
    return response["data"]


def getChannelInfo(channel):  # prints channel data
    info_url = url + "channels?broadcaster_id=" + getid(channel)
    response = requests.get(info_url, headers=headers).json()
    return response["data"][0]
