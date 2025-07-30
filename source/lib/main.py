from source.lib import filesys, GUI, api, cache


def run():

    FileSystem = filesys.FileSystem(['config', 'cache', 'tmp', 'log', '.userdata', '.pgmdata', '.api-c'])
    FileSystem.buildConfig(['local.yaml'], [])
    cache.init(FileSystem)

    #GUI.main()

    cache.syncAPI()
