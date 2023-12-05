from pysyncobj import SyncObj, SyncObjConf, replicated

class KVStorage(SyncObj):
    def __init__(self, selfAddress, partnerAddrs):
        conf = SyncObjConf()
        super(KVStorage, self).__init__(selfAddress, partnerAddrs, conf)
        self.__data = {}

    @replicated
    def put(self, key, value):
        # put operation , that sets the value of the key to be the provided value
        print("put key: ", key, " with value: ", value)
        self.__data[key] = value

    @replicated        
    def append(self, key, value):
        # append the Append operation, that adds the provided value to the value of the key
        print("append key: ", key, " with value: ", value)
        if key in self.__data:
            if isinstance(self.__data[key], list):
                self.__data[key].append(value)
            else:
                self.__data[key] = [self.__data[key], value]
        else:
            self.__data[key] = [value]

    def get(self, key):
        # get operation, that retrieves the value of the provided key
        print("get key: ", key)
        return self.__data.get(key, None)

    def get_dumpfile(self):
        return self.dumpFile
