import requests

headers = {"Client-ID": "aa00f8e0g4gic1bkruejtn1qvht9v3", "Authorization": "Bearer fd253rukwe5shngahs4eb1bzxlz7e8"}
url = "https://api.twitch.tv/helix/"


def extraction(choice, username):
    options = {
        "Top 20 games": getTop20Games,
        "Global Emotes": getGlobalEmotes,
        "Top 20 Streams": getTop20Streams,
        "Top 20 Soundtrack Playlists": getTop20SoundtrackPlaylists,
        "Global Chat Badges": getGlobalChatBadges,
        "Global Cheermotes": getGlobalCheermotes
    }
    return options[choice](username)


def getTop20Games(username):  # prints data of top 20 broadcasted games
    topgames_url = url + "games/top"
    response = requests.get(topgames_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalEmotes(username):  # prints data of all global emotes that are used in chat
    emote_url = url + "chat/emotes/global"
    response = requests.get(emote_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getTop20Streams(username):  # prints top 20 current streams
    stream_url = url + "streams"
    response = requests.get(stream_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getTop20SoundtrackPlaylists(username):  # prints top 20 Soundtrack Playlists
    music_url = url + "soundtrack/playlists"
    response = requests.get(music_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalChatBadges(username):  # prints all global chat badges
    badge_url = url + "chat/badges/global"
    response = requests.get(badge_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalCheermotes(username):  # prints all global chat badges
    cheer_url = url + "bits/cheermotes"
    response = requests.get(cheer_url, headers=headers).json()
    data = response["data"][0]["tiers"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result
