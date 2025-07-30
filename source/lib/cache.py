# this file will contain all the code to sotre data locally

from source.lib import api
global FileSystem


def init(fs):
    global FileSystem

    FileSystem = fs


def syncAPI():

    PATH = FileSystem.apiCachePath

    
