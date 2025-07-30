from source.lib import filesys, GUI, api


def run():

    FileSystem = filesys.FileSystem(['config', 'cache', 'tmp', 'log', '.userdata', '.pgmdata'])
    FileSystem.buildConfig(['local.yaml'], [])

    GUI.Main()
