import os
import subprocess


client_id = 'aa00f8e0g4gic1bkruejtn1qvht9v3'
client_secret = 'scpcq6f9io95x79pw1hhhb3yjiyxnu'
config_cmd = "twitch configure -i " + client_id + " -s " + client_secret
os.system('cmd /C ' + config_cmd)


username = input("Enter username: ")
id_cmd = "twitch api get /users -q login=" + username
data_dict = eval(subprocess.check_output(id_cmd,shell=True))
ID = data_dict['data'][0]['id']

#API DATA

def getUser(): #prints data of specific user
    user_cmd = "twitch api get /users -q login=" + username
    os.system('cmd /C ' + user_cmd)

def getTopGames(): #prints data of top 20 broadcasted games
    topgames_cmd = "twitch api get /games/top"
    os.system('cmd /C ' + topgames_cmd)

def getGame(): #prints data of specific game
    game = input("Enter game name: ")
    game_cmd = "twitch api get /games -q name=" + game
    os.system('cmd /C ' + game_cmd)

def getGlobalEmotes(): #prints data of all global emotes that are used in chat
    emote_cmd = "twitch api get /chat/emotes/global"
    os.system('cmd /C ' + emote_cmd)

def getStreams(): #prints all current streams
    stream_cmd = "twitch api get /streams"
    os.system('cmd /C ' + stream_cmd)

def getSoundtrackPlaylists(): #prints Soundtrack Playlists
    music_cmd = "twitch api get /soundtrack/playlists"
    os.system('cmd /C ' + music_cmd)

def getChannelFollowers(ID): 
    channel_cmd = 'twitch api get /channels/followers -q broadcaster_id='+ID
    os.system("cmd /C" + channel_cmd)

def getUsersFollows(ID):
    follows_cmd = 'twitch api get /users/follows -q from_id='+ID
    os.system("cmd /C" + follows_cmd)

def getUsersFollowing(ID):
    following_cmd = 'twitch api get /users/follows -q to_id='+ID
    os.system("cmd /C" + following_cmd)

def getVideoClip(ID):
    clip_cmd = 'twitch api get /clips -q broadcaster_id='+ID
    os.system("cmd /C" + clip_cmd)

def getChannelInfo(ID):
    Info_cmd = 'twitch api get /channels -q broadcaster_id='+ID
    os.system("cmd /C" + Info_cmd)



