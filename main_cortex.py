# -*- coding: utf-8 -*-
"""
APP Name:
"""
import Emotiv.Cortex_API

class CortexStuff():
    def __init__(self, url, user, clientID, clientSecret):
        self.cortex = Emotiv.Cortex_API.Cortex1(url, user)
        self.init(self.cortex, clientID, clientSecret)


    def init(self, cortex, clientID, clientSecret):
        stream = ["com"]
        profile_name = "Kyle"

        print('get cortex info')
        cortex.get_cortex_info()

        print('has_access_right')
        cortex.has_access_right(clientID, clientSecret)

        print('request access')
        cortex.request_access(clientID, clientSecret)

        print('authorize')
        cortex.authorize(clientID, clientSecret)

        print('query headsets')
        cortex.query_headset()

        # print('create profile')
        # cortex.create_profile()                    # can create a profile once. If it already exists, you will get an error if you run this

        print('load profile')
        cortex.load_profile(profile_name)

        # print('unload profile')
        # cortex.unload_profile()

        print('session create')
        cortex.create_session()

        print('activate session')
        cortex.activate_session()


    def start(self, cortex):
        stream = ["com"]
        print('subscribe')
        cortex.subscribe(stream)

        cortex.close_session()
        print('close session')


# client secret: UhXMbqIye06FF7bnPa3S3kbKUMHUmUlQyythjmEwrkVdmoY7gsPjtqeeR3y8kfrvboPgiKVNuT77CCN8OyiHaOYyb8dUqk2Zk1vB9SwTaR7XUCJYtHT0ZYqkhctpXPq8
# client id: rhw7Lf0Z7AKLKJIajwEiYnbAJ9cX87CwnJJJEPtf
# app id: com.chantal2.rocket
# app name: Rocket
# username = chantal2

url = "wss://localhost:6868"
clientID = 'rhw7Lf0Z7AKLKJIajwEiYnbAJ9cX87CwnJJJEPtf'
clientSecret = 'UhXMbqIye06FF7bnPa3S3kbKUMHUmUlQyythjmEwrkVdmoY7gsPjtqeeR3y8kfrvboPgiKVNuT77CCN8OyiHaOYyb8dUqk2Zk1vB9SwTaR7XUCJYtHT0ZYqkhctpXPq8'
user = {
    'clientId': clientID,

    'clientSecret': clientSecret

    , "number_row_data": 100
    # change this value to control the number of times the loop is ran to generate actions and scores
}
