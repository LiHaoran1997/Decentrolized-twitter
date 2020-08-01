import json
import requests
import httplib2
import urllib
import random



class BlockChain:
    token = ""
    host = "localhost"
    port = 4000
    def __init__(self):
        self.token= self.getToken()

    def getToken(self):
        url = 'https://localhost:4000/admins'
        data = "username=admin_cc_gfe&orgname=Gfe"
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        conn = httplib2.Http()
        res1,res2=conn.request('http://localhost:4000/admins','POST',  data, headers)
        try:
            jsondata=json.loads(res2)
            token=jsondata['token']
            print(token)
        except ValueError as e:
            print(e)
        # conn.close()
        return token

    def blockChainPut(self,key,value):
        key=key.encode("utf8").decode("latin-1")
        value=value.encode("utf8").decode("latin-1")
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"weibo\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"Put\",\n" +\
                    "\t\"args\":[\""+key+"\",\""+value+"\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/weibo', data, headers)
        try:
            httpres = conn.getresponse()
            return httpres.read()
        except ValueError as e:
            print(e)

    def blockChainQueryByKey(self,key):
        key=key.encode("utf8").decode("latin-1")
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"weibo\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"QueryByKey\",\n" +\
                    "\t\"args\":[\""+key+"\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/weibo', data, headers)
        try:
            httpres = conn.getresponse()
            res=str(httpres.read(),encoding="utf-8")
            return res
        except ValueError as e:
            print(e)

    def blockChainDelete(self,key):
        key=key.encode("utf8").decode("latin-1")
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"weibo\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"Delete\",\n" +\
                    "\t\"args\":[\""+key+"\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/weibo', data, headers)
        try:
            httpres = conn.getresponse()
            res=str(httpres.read(),encoding="utf-8")
            return res
        except ValueError as e:
            print(e)


    def blockChainInitCoin(self):
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"coin\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"initLedger\",\n" +\
                    "\t\"args\":[\"WBCoin\",\"WeiboCoin\",\"99999999999\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/coin', data, headers)
        try:
            httpres = conn.getresponse()
            return httpres.read()
        except ValueError as e:
            print(e)

    def blockChainInitCoin(self):
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"coin\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"initLedger\",\n" +\
                    "\t\"args\":[\"WBCoin\",\"WeiboCoin\",\"999999999999\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/coin', data, headers)
        try:
            httpres = conn.getresponse()
            return httpres.read()
        except ValueError as e:
            print(e)

    def blockChainTransferToken(self,_from,_to,_amount):
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"coin\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"transferToken\",\n" +\
                    "\t\"args\":[\"WBCoin\",\""+_from+"\",\""+_to+"\",\""+_amount+"\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/coin', data, headers)
        try:
            httpres = conn.getresponse()
            return httpres.read()
        except ValueError as e:
            print(e)

    def blockChainbalanceToken(self,account):
        data = "{"+"\"peers\": [\"peer0.fabric.gfe.com\"],\n" +\
                    "\t\"chaincodeName\":\"coin\",\n" +\
                    "\t\"chaincodeVersion\":\"v0\",\n" +\
                    "\t\"chaincodeType\": \"go\",\n" +\
                    "\t\"fcn\":\"balanceToken\",\n" +\
                    "\t\"args\":[\"WBCoin\",\""+account+"\"]\n" +\
                    "}"
        headers = {'authorization':"Bearer "+self.token,'content-type': 'application/json'}
        conn = httplib2.HTTPConnectionWithTimeout(self.host+':'+str(self.port))
        conn.request('POST', '/channels/softwarechannel/chaincodes/coin', data, headers)
        try:
            httpres = conn.getresponse()
            return httpres.read()
        except ValueError as e:
            print(e)
blk=BlockChain()
print(blk.blockChainQueryByKey("weibo.user.152"))
# # print(blk.blockChainTransferToken("coinbase","213","10000"))
# print(str(blk.blockChainbalanceToken("233"),encoding='utf8'))
# print(blk.blockChainPut("test2","good"))
# print(blk.blockChainQueryByKey("test2"))
# print(blk.blockChainDelete("test2"))
# print(random.randint(0, 20)/100)
