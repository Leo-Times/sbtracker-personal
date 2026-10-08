import requests
import datetime  
import json
import time
from pprint import pprint 

def frozen_data():
    name = "frozen_emerald"
    grab_id_player = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name)
    id_data = (json.loads(grab_id_player.text))
    player_id = id_data['id']

    key = "5df8347e-4bb6-4a02-8003-83b81b95cbba"

    player_profile_url = "https://api.hypixel.net/v2/skyblock/profiles?key=" + key + "&uuid=" + player_id
    player = requests.get(player_profile_url)
    player_data_Json = json.loads(player.text)
    player_data_Json == player.json()

    money = (player_data_Json['profiles'][0]["members"][player_id]["profile"]["bank_account"]) + (player_data_Json['profiles'][0]["members"][player_id]["currencies"]["coin_purse"])

    skills = (player_data_Json['profiles'][0]["members"][player_id]["player_data"]["experience"]) 

    return money, skills

def jeved_data():
    name = "jeved"
    grab_id_player = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name)
    id_data = (json.loads(grab_id_player.text))
    player_id = id_data['id']

    name = "shoderHD"
    grab_id_player = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name)
    id_data = (json.loads(grab_id_player.text))
    shoder_id = id_data['id']

    key = "5df8347e-4bb6-4a02-8003-83b81b95cbba"

    player_profile_url = "https://api.hypixel.net/v2/skyblock/profiles?key=" + key + "&uuid=" + player_id
    player = requests.get(player_profile_url)
    player_data_Json = json.loads(player.text)
    player_data_Json == player.json()

    money = (player_data_Json['profiles'][2]["banking"]["balance"]) + (player_data_Json['profiles'][2]["members"][player_id]["currencies"]["coin_purse"]) + (player_data_Json['profiles'][2]["members"][shoder_id]["currencies"]["coin_purse"])

    skills = (player_data_Json['profiles'][2]["members"][player_id]["player_data"]["experience"]) 

    return money, skills

def time_formater():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    return [day, month, year, hour, minute]

def json_data_adder():
    data_F = frozen_data()
    data_J = jeved_data()

    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    data["player"]["Frozen_Emerald"]["money"].append(data_F[0])
    data["player"]["Jeved"]["money"].append(data_J[0])

    for key in data_F[1].keys():
        data["player"]["Frozen_Emerald"]["skills"][key].append(data_F[1][key])

    for key in data_J[1].keys():
            data["player"]["Jeved"]["skills"][key].append(data_J[1][key])

    data["Time"].append(time_formater())

    with open('data.json', 'w', encoding='utf-8') as file:
         json.dump(data, file)   

while True:
    if datetime.datetime.now().minute == 15 or datetime.datetime.now().minute == 45 or datetime.datetime.now().minute == 30 or datetime.datetime.now().minute == 0: 
        json_data_adder()
        time.sleep(100)
    time.sleep(50)
