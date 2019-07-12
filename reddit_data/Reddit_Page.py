class Reddit_Page:
    def _init_(self,kind,data):
        self.kind = kind
        self.data = Reddit_Data(data["children"],data["after"])
        

    @staticmethod
    def fromJson(page):
        return Reddit_Page(page["kind"],page["data"])
        
     


