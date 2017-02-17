#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script allows you to read and write settings of an application.
There are the following settings:
- "CultureCode" - like 'ru-RU', obligatory.
- "Servers" - a list of servers, where each server is described by the following attributes:
    - "ID" - integer, unique, obligatory.
    - "ServerName" - string, obligatory.
    - "ServerPort" - integer, obligatory.
    - "UserName" - string, optional (if not specified, a user must enter it when runs the application).
    - "Password" - string, optional (if not specified, a user must enter it when runs the application).
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
                'Servers': [
                    {1: {'ServerName': 'LOCALHOST', 'ServerPort': 1017,
                     'UserName': '', 'Password': ''}}
                ]}
        return data

    def __is_valid(self, data):
        if isinstance(data, dict) and \
            len(data) == 2 and \
            data.has_key('CultureCode') and data.has_key('Servers') and \
            isinstance(data['CultureCode'], str) and \
            (len(data['CultureCode']) == 2 or len(data['CultureCode']) == 5) and \
            isinstance(data['Servers'], list):
                all_servers_correct = False
                for server in  data['Servers']:
                    if isinstance(server, dict) and \
                        len(server) == 1:
                            for serv_id in  server.keys():
                                if isinstance(serv_id, int):
                                    all_servers_correct = True
                                else:
                                    return False
                            for serv_details in server.values():
                                if isinstance(serv_details, dict) and \
                                    len(serv_details) == 4 and \
                                    serv_details.has_key('ServerName') and \
                                    serv_details.has_key('ServerPort') and \
                                    serv_details.has_key('UserName') and \
                                    serv_details.has_key('Password') and \
                                    isinstance(serv_details['ServerPort'], int) and \
                                    isinstance(serv_details['ServerName'], str) and \
                                    isinstance(serv_details['UserName'], str) and \
                                    isinstance(serv_details['Password'], str) and \
                                    len(serv_details['ServerName']) >= 1 and \
                                    len(serv_details['ServerPort']) >= 1:
                                        all_servers_correct = True
                                else:
                                    return False
                            else:
                                return False
                    else:
                        return False
                return all_servers_correct
        else:
            return False

    def __read_file(self):
        if os.path.exists(self.filePath):
            data = json.load(open(self.filePath, 'r'))
        else:
            data = self.__create_default()
        if self.__is_valid(data):
            return data

    def __write_file(self):
        if self.__is_valid(data):
            json.dump(self.__data, open(self.filePath, 'w'), indent=4)

    def get_settings(self):
        return self.__data

    def set_cultureCode(self, newCode):
            self.__data['CultureCode'] = newCode
            self.__write_file()

    def edit_serverByID(self, serverID, serverName = None,
                        serverPort = None, userName = None, password = None):
        if isinstance(serverID, int):
            pass

"""ОСТАНОВИЛСЯ ЗДЕСЬ
В этом классе надо дописать, как обновить атрибуты сервера, не забыть возможность задавать имя и пароль юзера пустой строкой - смю isinstance('', type(None))

Дальше надо сделать методы для добавления и удаления серверов, а также получение текущей папки.

"""



mySettings = Settings(r'C:\Users\Alexey\Documents\GitHub\CGScripting\4. Text files\appSettings.config')


print mySettings.get_settings()

mySettings.set_cultureCode('en-US')

print mySettings.get_settings()



