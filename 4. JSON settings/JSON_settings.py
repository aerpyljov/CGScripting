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

It is recommended to run the script in a console, not by a double mouse click.
"""

import os
import json


class Settings(object):
    """Read and write app settings using a JSON file"""
    def __init__(self, folder=None, filename=None):
        if not folder:
            folder = os.path.dirname(os.path.abspath(__file__))
        if not filename:
            filename = 'appSettings.config'
        self.filePath = os.path.join(folder, filename)
        self.__data = self.__read_file()
        self.__write_file()

    @staticmethod
    def __create_default():
        data = {'CultureCode': 'ru-RU',
                'Servers':
                    {
                        '1': {'ServerName': 'LOCALHOST', 'ServerPort': 1017,
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
        if isinstance(data, dict) and \
          'CultureCode' in data and 'Servers' in data:
            return True
        else:
            print 'Settings structure invalid:\n{0}'.format(data)
            return False

    @classmethod
    def __culturecode_valid(cls, data):
        """Culture code must be like 'ru' or 'ru-RU'"""
        code = data['CultureCode']
        if (isinstance(code, str) or isinstance(code, unicode)) and \
          (len(code) == 2 or len(code) == 5):
            return True
        else:
            print 'Culture Code invalid - {0}'.format(code)
            return False

    @classmethod
    def __serverlist_valid(cls, data):
        """Servers must be a non-empty dictionary, where each server is valid"""
        servers = data['Servers']
        if isinstance(servers, dict) and servers:
            for server_id in servers:
                server = servers[server_id]
                if not cls.__server_valid(server):
                    return False
            return True
        else:
            print 'List of servers invalid:\n{0}'.format(servers)
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
            print 'Server invalid:\n{0}'.format(server)
            return False

    def __read_file(self):
        if os.path.exists(self.filePath):
            data = json.load(open(self.filePath, 'r'))
            print 'File with settings exists'
        else:
            data = self.__create_default()
            print 'New file with default settings created'
        if self.__settings_valid(data):
            return data
        else:
            print 'Cannot read incorrect settings'

    def __write_file(self):
        data = self.__data
        if self.__settings_valid(data):
            json.dump(data, open(self.filePath, 'w'), indent=4)
        else:
            print 'Cannot write incorrect settings'
            self.__data = self.__read_file()

    def get_settings(self):
        return self.__data

    def set_culture_code(self, new_code):
            self.__data['CultureCode'] = new_code
            self.__write_file()

    def add_server(self, server_id, server_name,
            server_port, username='', password=''):
        servers = self.__data['Servers']
        server_id = unicode(server_id)
        if server_id not in servers:
            servers[server_id] = {}
            new_server = servers[server_id]
            new_server['ServerName'] = server_name
            new_server['ServerPort'] = server_port
            new_server['UserName'] = username
            new_server['Password'] = password
            self.__write_file()
        else:
            print 'Server with ID = {0} already exists'.format(server_id)

    def edit_server(self, server_id, server_name=None,
            server_port=None, username=None, password=None):
        servers = self.__data['Servers']
        server_id = unicode(server_id)
        if server_id in servers:
            server = servers[server_id]
            if server_name is not None:
                server['ServerName'] = server_name
            if server_port is not None:
                server['ServerPort'] = server_port
            if username is not None:
                server['UserName'] = username
            if password is not None:
                server['Password'] = password
            self.__write_file()
        else:
            print 'There is no server with ID = {0}'.format(server_id)

    def remove_server(self, server_id):
        servers = self.__data['Servers']
        server_id = unicode(server_id)
        servers.pop(server_id, False)
        self.__write_file()



"""
TEST
"""

"""Correct settings"""
print "\n===Create an instance of Settings class==="
mySettings = Settings()

print "\n===Settings at the beginning==="
print mySettings.get_settings()

print "\n===New culture code - must be 'en-US'==="
mySettings.set_culture_code('en-US')
print mySettings.get_settings()['CultureCode']

print "\n===New server added (ID = 8)==="
mySettings.add_server(server_id=8, server_name='MAIN_SERVER',
            server_port=8088, username='Vasya', password='')
print mySettings.get_settings()['Servers']

print "\n===For server with ID = 1 server_name changed to 'SECONDARY_SERVER'==="
mySettings.edit_server(server_id=1, server_name='SECONDARY_SERVER')
print mySettings.get_settings()['Servers']

print "\n===Server with ID = 1 removed==="
mySettings.remove_server(server_id=1)
print mySettings.get_settings()['Servers']


"""Incorrect settings"""

print "\n===Create a new instance of Settings class==="
newSettings = Settings()

print "\n===Settings at the beginning==="
print newSettings.get_settings()

print "\n===New culture code - try 'English' (incorrect)==="
newSettings.set_culture_code('English')
print 'Real culture code - ', newSettings.get_settings()['CultureCode']

print "\n===New server added (ID = 9) - empty server_name and server_port (incorrect)==="
newSettings.add_server(server_id=9, server_name='',
            server_port='', username='Petr', password='qwerty')
print 'Real list of servers - ', newSettings.get_settings()['Servers']

print "\n===For server with ID = 8 server_port changed to an empty string (incorrect)==="
newSettings.edit_server(server_id=8, server_port='')
print 'Real list of servers - ', newSettings.get_settings()['Servers']

print "\n===All servers removed (incorrect)==="
newSettings.remove_server(server_id=8)
print 'Real list of servers - ', newSettings.get_settings()['Servers']

print "\n===New server added with ID, that already exists (ID = 8) (incorrect)==="
newSettings.add_server(server_id=8, server_name='DEV_SERVER',
            server_port=9999, username='', password='')
print newSettings.get_settings()['Servers']

print "\n===Settings after all changes==="
print 'Real settings - ', newSettings.get_settings()

