import requests

headers = {"Client-ID": "kdtctg61dvdiw8is5kpevgdqrxem6e", "Authorization": "Bearer vc0sxm59vprzmi8pti3eyakwf5rb57"}
url = "https://api.twitch.tv/helix/"


def extraction(choice):
    options = {
        "Top 20 games": getTop20Games,
        "Global Emotes": getGlobalEmotes,
        "Top 20 Streams": getTop20Streams,
        "Top 20 Soundtrack Playlists": getTop20SoundtrackPlaylists,
        "Global Chat Badges": getGlobalChatBadges,
        "Global Cheermotes": getGlobalCheermotes
    }
    return options[choice]()


def getTop20Games():  # prints data of top 20 broadcasted games
    topgames_url = url + "games/top"
    response = requests.get(topgames_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalEmotes():  # prints data of all global emotes that are used in chat
    emote_url = url + "chat/emotes/global"
    response = requests.get(emote_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getTop20Streams():  # prints top 20 current streams
    stream_url = url + "streams"
    response = requests.get(stream_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getTop20SoundtrackPlaylists():  # prints top 20 Soundtrack Playlists
    music_url = url + "soundtrack/playlists"
    response = requests.get(music_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalChatBadges():  # prints all global chat badges
    badge_url = url + "chat/badges/global"
    response = requests.get(badge_url, headers=headers).json()
    data = response["data"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result


def getGlobalCheermotes():  # prints all global cheermotes
    cheer_url = url + "bits/cheermotes"
    response = requests.get(cheer_url, headers=headers).json()
    data = response["data"][0]["tiers"]
    result = ""
    for i in data:
        result += str(i) + '\n'
    return result
