#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script allows you to read and write settings of an application.
There are the following settings:
- "CultureCode" - like 'ru' or 'ru-RU', obligatory.
- "Servers" - a non-empty dictionary of servers, where each server is described by the following attributes:
    - "ID" - a dictionary key - unique, obligatory.
    - "ServerName" - obligatory.
    - "ServerPort" - obligatory.
    - "UserName" - optional (if not specified, a user must enter it when runs the application).
    - "Password" - optional (if not specified, a user must enter it when runs the application).
"""

import os
import json


class Settings(object):
    """Read and write app settings using a JSON file"""
    def __init__(self, path):
        self.filePath = path
        self.__data = self.__read_file()
        self.__write_file()

    @staticmethod
    def __create_default():
        data = {'CultureCode': 'ru-RU',
                'Servers':
                    {
                        1: {'ServerName': 'LOCALHOST', 'ServerPort': 1017,
                            'UserName': '', 'Password': ''}
                    }
                }
        return data

    @classmethod
    def __settings_valid(cls, data):
        if cls.__settigs_structure_valid(data) and \
          cls.__culturecode_valid(data) and cls.__serverlist_valid(data):
            return True
        else:
            return False

    @classmethod
    def __settigs_structure_valid(cls, data):
        """Must be a dictionary with 2 keys"""
        if isinstance(data, dict) and len(data) == 2 and \
          'CultureCode' in data and 'Servers' in data:
            return True
        else:
            return False

    @classmethod
    def __culturecode_valid(cls, data):
        """Culture code must be like 'ru' or 'ru-RU'"""
        code = data['CultureCode']
        if isinstance(code, str) and \
          (len(code) == 2 or len(code) == 5):
            return True
        else:
            return False

    @classmethod
    def __serverlist_valid(cls, data):
        """Servers must be a non-empty dictionary, where each server is valid"""
        servers = data['Servers']
        if isinstance(servers, dict) and servers:
            for server in servers:
                if not cls.__server_valid(server):
                    return False
            return True
        else:
            return False

    @classmethod
    def __server_valid(cls, server):
        """Server must be a dictionary with 4 keys, and 2 of them cannot be empty"""
        if isinstance(server, dict) and \
          'ServerName' in server and 'ServerPort' in server and \
          'UserName' in server and 'Password' in server and \
          server['ServerName'] and server['ServerPort']:
            return True
        else:
            return False

    def __read_file(self):
        if os.path.exists(self.filePath):
            data = json.load(open(self.filePath, 'r'))
        else:
            data = self.__create_default()
        if self.__settings_valid(data):
            return data

    def __write_file(self):
        data = self.__data
        if self.__settings_valid(data):
            json.dump(data, open(self.filePath, 'w'), indent=4)

    def get_settings(self):
        return self.__data

    def set_culture_code(self, new_code):
            self.__data['CultureCode'] = new_code
            self.__write_file()

    def add_edit_server(self, server_id, server_name = None,
            server_port = None, username = None, password = None):
        servers = self.__data['Servers']
        if server_id not in servers:
            servers[server_id] = {}
        server = servers[server_id]
        server['ServerName'] = server_name
        server['ServerPort'] = server_port
        server['UserName'] = username
        server['Password'] = password
        self.__write_file()

    def remove_server(self, server_id):
        servers = self.__data['Servers']
        servers.pop(server_id, False)
        self.__write_file()



"""
TEST
"""



mySettings = Settings(r'C:\Users\Alexey\Documents\GitHub\CGScripting\4. Text files\appSettings.config')


print mySettings.get_settings()

mySettings.set_culture_code('en-US')

print mySettings.get_settings()



