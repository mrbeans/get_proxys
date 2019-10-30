class BaseModel(object):
    def __init__(self,ip,port,protocal,region):
        self.IP=ip
        self.Port=port
        self.Protocal=protocal
        self.Region=region
    
    def to_dict(self):
        return {
            'ip':self.IP,
            'port':self.Port,
            'protocal':self.Protocal,
            'region':self.Region
        }