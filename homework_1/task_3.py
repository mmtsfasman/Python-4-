class UniqObject(object):
    __instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UniqObject, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def create_object(cls):
        if not cls.__instance:
            cls.__instance = UniqObject()
        return cls.__instance

   
