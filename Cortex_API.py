# -*- coding: utf-8 -*-

"""
Cortex API functionality from Cortex 2.0 Gitbook

TODO: test self.headset_id, do I need to return the headset id or can I just directly
call it with self
"""
import json
import random
import ssl
import time
import random

import websocket  # install with pip install websocket-client
import keyboard


class Cortex1():
    def __init__(self, url, user):
        self.ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
        self.user = user
        self.action = ""

    def query_headset(self):
        queryheadset_request = {
            'id': 2,
            "jsonrpc": "2.0",
            "method": "queryHeadsets",
            "params": {}
        }
        self.ws.send(json.dumps(queryheadset_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        self.headset_id = result_dic['result'][0]['id']
        return self.headset_id
        # print('headset_id', self.headset_id)
        # print('query headset result', json.dumps(result_dic, indent=4))

    def connect_headset(self):
        connect_headset_request = {
            "jsonrpc": "2.0",
            "id": 111,
            "method": "controlDevice",
            "params": {
                "command": "connect",
                "headset": self.headset_id
            }
        }
        self.ws.send(json.dumps(connect_headset_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('connect headset result', json.dumps(result_dic, indent=4))

    def request_access(self, clientID, clientSecret):
        request_access_request = {
            "jsonrpc": "2.0",
            "method": "requestAccess",
            "params": {
                'clientId': clientID,
                'clientSecret': clientSecret
            },
            "id": 1
        }
        self.ws.send(json.dumps(request_access_request))
        result = self.ws.recv()
        result_dic = json.loads(result)

    def authorize(self, clientID, clientSecret):
        authorize_request = {
            "jsonrpc": "2.0",
            "method": "authorize",
            "params": {
                'clientId': clientID,
                'clientSecret': clientSecret,
                'debit': 1,
            },
            "id": 4
        }
        self.ws.send(json.dumps(authorize_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('auth_result', json.dumps(result_dic, indent=4))
        self.auth = result_dic['result']['cortexToken']
        # print('\ncortexToken', self.auth)

    def create_session(self):
        create_session_request = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "createSession",
            "params": {
                "cortexToken": self.auth,
                "headset": self.headset_id,
                "status": "open"
            }
        }
        self.ws.send(json.dumps(create_session_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('create session result ', json.dumps(result_dic, indent=4))
        self.session_id = result_dic['result']['id']
        # print(self.session_id)
        return self.session_id

    def activate_session(self):
        activate_session_request = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "updateSession",
            "params": {
                "cortexToken": self.auth,
                "session": self.session_id,
                "status": "active"
            }
        }
        self.ws.send(json.dumps(activate_session_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('activate session result ', json.dumps(result_dic, indent=4))
        self.session_id = result_dic['result']['id']
        # print(self.session_id)

    def create_profile(self):
        create_request = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "setupProfile",
            "params": {
                "cortexToken": self.auth,
                "profile": "user1",  # Add profile name here
                "status": "create"
            }
        }
        self.ws.send(json.dumps(create_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        print(result_dic)
        # print('creating profile', json.dumps(result_dic, indent=4))
        self.name = result_dic['result']['name']  # assigning object .name attribute to cortex object
        print(self.name)
        return self.name

    def load_profile(self, profile_name):
        load_request = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "setupProfile",
            "params": {
                "cortexToken": self.auth,
                'headset': self.headset_id,
                "profile": profile_name,
                'status': 'load'
            }
        }
        self.ws.send(json.dumps(load_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('loading up profile', json.dumps(result_dic, indent=4))
        return result_dic

    def unload_profile(self):
        unload_request = {
            "id": 3,
            "jsonrpc": "2.0",
            "method": "setupProfile",
            "params": {
                "cortexToken": self.auth,
                'profile': self.name,
                'headset': self.headset_id,
                'status': 'unload'
            }}
        self.ws.send(json.dumps(unload_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        print('unloading up profile', json.dumps(result_dic, indent=4))

    def close_session(self):
        close_session_request = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "updateSession",
            "params": {
                "cortexToken": self.auth,
                "session": self.session_id,
                "status": "close"
            }
        }
        self.ws.send(json.dumps(close_session_request))
        result = self.ws.recv()
        result_dic = json.loads(result)
        # print('close session result ', json.dumps(result_dic, indent=4))

    def get_cortex_info(self):
        get_cortex_info_request = {
            "jsonrpc": "2.0",
            "method": "getCortexInfo",
            "id": 100
        }
        self.ws.send(json.dumps(get_cortex_info_request))
        result = self.ws.recv()
        # print(json.dumps(json.loads(result), indent=4))

    def has_access_right(self, clientID, clientSecret):
        has_access_right_request = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "hasAccessRight",
            "params": {
                'clientId': clientID,
                'clientSecret': clientSecret
            }
        }
        self.ws.send(json.dumps(has_access_right_request))
        result = self.ws.recv()
        # print(json.dumps(json.loads(result), indent=4))

    # def grant_access_and_session_info(self): # can call this function in main.py to run all the other functions inside of it
    #     self.query_headset()
    #     self.connect_headset()
    #     self.request_access()
    #     self.authorize()
    #     self.create_session(self.auth, self.headset_id)

    def subRequest(self, stream):
        subRequest = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "params": {
                "cortexToken": self.auth,
                "session": self.session_id,
                "streams": stream
            },
            "id": 6
        }

        self.ws.send(json.dumps(subRequest))

        print('\n')
        print('subscribe result')

        # for i in range(1, self.user['number_row_data']):                    # Modify for loop to run however many times
        stop = 1
        while stop:
            new_data = self.ws.recv()
            result_dic = json.loads(new_data)
            self.extractKeyValue(result_dic)
            time.sleep(0.01)

            if (keyboard.is_pressed('q')):
                stop = 0

    def subscribe(self, stream):
        # self.grant_access_and_session_info()
        self.subRequest(stream)
        print('subscribed to session')  # calling function to get mental command info

    def extractKeyValue(self, result_dic):

        first_response = {
            "id": 6,
            "jsonrpc": "2.0",
            "result": {
                "failure": [],
                "success": [{
                    "cols": ["act", "pow"],
                    "sid": self.session_id,
                    "streamName": "com"
                }]
            }
        }
        #    neutral = ['neutral', 0.0]

        self.l = ''
        if result_dic != first_response:
            self.get_mental_command = result_dic['com']
            print("action updated")

            # if (self.get_mental_command[0] == 'right') and (self.get_mental_command[1] > 0.15):
            #     action = self.get_mental_command[0]
            #     score = str(self.get_mental_command[1])
            #     #print('action:', action + ',' + ' score:', score)

            if self.get_mental_command[1] > 0.1:
                self.action = self.get_mental_command[0]
                score = str(self.get_mental_command[1])
                print(self.action)
                #print('action:', self.action, ',', ' score:', score)

            return self.l
