import http.client
import mimetypes
import json
import ssl
import pyotp
import constants

class Auth:

    def getConnection(self):
        return http.client.HTTPSConnection(constants.TRANSACTION_ENDPOINT, context = ssl._create_unverified_context())
    
    def login(self):
        connection= self.getConnection()
        # with open(constants.LOGIN_PAYLOAD) as f:
        payload = {}
        payload["clientcode"] = constants.CLIENTCODE
        payload["password"] = constants.PASSWORD
        payload["totp"] = pyotp.TOTP(constants.TOTP).now()
        dumpedPayload=json.dumps(payload)

        headers= json.loads(open(constants.HEADERS_PAYLOAD).read())
        connection.request("POST", constants.LOGIN_RESOURCE , dumpedPayload, headers)
        headers["Authorization"]= "Bearer "+json.loads(connection.getresponse().read().decode("utf-8"))["data"]["jwtToken"]
        return headers