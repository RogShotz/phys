# -*- coding: UTF-8 -*-
import requests
import time
import json

# Go to Hypixel and type /api for your API key.
# Enter Your Api in The " " below (It's only for Hypixel to know who is sending requests to their API site)
key = "42bf9e6f-60fe-469d-bd75-c23b761eaf6a"
apifg = "https://api.hypixel.net/findGuild"
apigl = "https://api.hypixel.net/guild"
apifl = "https://api.hypixel.net/friends"

# Put your Guild's UUID Key Here
# Will Put Link in the Forum Post on how to get the Guild's UUID
uuid_mm = "5e012bc38ea8c92086b10aa7"


def name2uuid(name):
    getReq = requests.get(url="https://playerdb.co/api/player/minecraft/" + name)
    if getReq.content == "":
        print("[ERROR] Empty Response.")
        return ""
    getJson = json.loads(getReq.content.decode('utf-8'))
    if getJson["success"] != True:
        print("[ERROR] Name->UUID API Failed.")
        print('Attempted Name: ', name)
        print(getJson)
        return ""
    ret = getJson["data"]["player"]["raw_id"]
    return ret


def uuid2name(uuid):
    getReq = requests.get(url="https://playerdb.co/api/player/minecraft/" + uuid)
    if getReq.content == "":
        print("[ERROR] Empty Response.")
        return ""
    getJson = json.loads(getReq.content.decode('utf-8'))
    if getJson["success"] != True:
        print("[ERROR] API Failed. Response:")
        print(getJson)
        print("Attempted uuid: ", uuid)
        return ""
    ret = getJson["data"]["player"]["username"]
    return ret


def getGuildMember(uuid):
    AcReq = requests.get(url=apigl, params={"key": key, "id": uuid_mm})
    AcJson = json.loads(AcReq.content.decode('utf-8'))
    mbjson = AcJson["guild"]["members"]
    ret = []
    for i in range(0, len(mbjson)):
        ret.append(mbjson[i]["uuid"])
    return ret


mm_memb = getGuildMember(uuid_mm)
print("Retrieved Guild Member Data.")


def isPlayerInGuild(uuid):
    if mm_memb.count(uuid) == 0:
        return 0
    else:
        return 1


def pullFriendData(uuid):
    AcReq = requests.get(url=apifl, params={"key": key, "uuid": uuid})
    AcJson = json.loads(AcReq.content.decode('utf-8'))
    recordsJson = AcJson["records"]
    ret = []
    target = ""
    for i in range(0, len(recordsJson)):
        if recordsJson[i]["uuidSender"] == uuid:
            target = recordsJson[i]["uuidReceiver"]
        else:
            target = recordsJson[i]["uuidSender"]
        ret.append(target)
    return ret


tabList = []
leecherList = []
# Whitelisted Player APIs go here
whiteList = [""]


def getSuspect(uuid):
    print("Leecher: ", uuid2name(uuid))
    suspectList = pullFriendData(uuid)
    for i in range(0, len(suspectList)):
        if isPlayerInGuild(suspectList[i]):
            if tabList.count(suspectList[i]):
                print("   Suspect:", uuid2name(suspectList[i]), "(MM)")
            else:
                print("   Suspect:", uuid2name(suspectList[i]), "(MM)")
        elif tabList.count(suspectList[i]):
            print("   Related Leecher:", uuid2name(suspectList[i]))


print("Converting All Names -> UUID...")
# Make Notepad File Named list.txt and save it in the same file as this program. This allows the program to function without it getting too complicated.
f = open("list.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip('\n')
    puuid = name2uuid(line)
    if puuid == "":
        continue
    if whiteList.count(puuid):
        print("Ignoring whitelisted player: ", line)
        continue
    tabList.append(puuid)
print("UUIDs retrieved, start checking...")

for i in tabList:
    if isPlayerInGuild(i) == 0:
        leecherList.append(i)

print("Total Leecher Count:", len(leecherList))

for i in leecherList:
    getSuspect(i)

f.close()