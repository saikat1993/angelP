import http.client
import mimetypes
import json
import ssl
import pyotp
import constants
import datetime;
from auth import Auth

class PlaceOrders:

    def __init__(self):
        self.auth = Auth()
        self.connection = self.auth.getConnection()
        self.headers = self.auth.login()


# B S SL
    def placeOrder(self, orderType, lot, sl=10):
        resource= "placeOrder"
        with open(constants.PLACEORDER_PAYLOAD) as f:
            with open(constants.CURRENT_STRIKE_DATA_PATH) as g:
                payload = json.load(f)
                currentScript = json.load(g)
                payload["tradingsymbol"] = currentScript["symbol"]
                payload["symboltoken"] = currentScript["token"]
                payload["exchange"] = currentScript["exch_seg"]
                payload["quantity"] = int(currentScript["lotsize"]) * lot

        if str(orderType).upper() == "B":
            payload["transactiontype"] = "BUY"

        elif str(orderType).upper() == "S":
            self.cancelActiveOpenOrder()
            payload["transactiontype"] = "SELL"
            
        elif str(orderType).upper() == "SL":
            payload["ordertype"] = "STOPLOSS_LIMIT"
            payload["variety"] = "STOPLOSS"
            payload["transactiontype"] = "SELL"
            payload["triggerprice"] = str(self.getLTP(currentScript) - (sl-2))
            payload["price"]= str(self.getLTP(currentScript) - sl)

        elif str(orderType).upper() == "MSL":
            # print(self.getOrderId())
            resource ="modifyOrder"
            payload["ordertype"] = "STOPLOSS_LIMIT"
            payload["variety"] = "STOPLOSS"
            payload["transactiontype"] = "SELL"
            payload["orderid"] = self.getOrderId()
            payload["triggerprice"] = str(self.getLTP(currentScript) - (sl-2))
            payload["price"]= str(self.getLTP(currentScript) - sl)

        payload = json.dumps(payload)
        self.connection.request("POST", constants.API_VERSION_RESOURCE+resource, payload, self.headers)
        placeOrderResponse = json.loads( self.connection.getresponse().read().decode("utf-8"))
        print(json.dumps(placeOrderResponse))

        with open('temp/activeTrade.json', 'w') as json_file:
            json_file.write(json.dumps(placeOrderResponse))
        return payload


    def getLTP(self, currentScript):
        payload = {}
        payload["tradingsymbol"] = currentScript["symbol"]
        payload["symboltoken"] = currentScript["token"]
        payload["exchange"] = currentScript["exch_seg"]

        payload = json.dumps(payload)
        self.connection.request("POST", constants.GET_LTP_DATA_RESOURCE, payload, self.headers)
        getLtpResponse = json.loads( self.connection.getresponse().read().decode("utf-8"))
        return float(getLtpResponse["data"]["ltp"])
        
    def cancelActiveOpenOrder(self):
        with open(constants.ACTIVE_TRADE_PAYLOAD) as f:
            with open(constants.CANCEL_ORDER_PAYLOAD) as g:
                activeTrade = json.load(f)
                cancelOrder = json.load(g)
                cancelOrder["orderid"]=  activeTrade["data"]["orderid"]
                dumpedCancelOrder = json.dumps(cancelOrder)

        self.connection.request("POST", constants.CANCEL_ORDER_RESOURCE, dumpedCancelOrder, self.headers)
        cancelOrderResponse = json.loads(self.connection.getresponse().read().decode("utf-8"))
        print(cancelOrderResponse)

    def getOrderId(self):
         with open(constants.ACTIVE_TRADE_PAYLOAD) as f:
                activeTrade = json.load(f)
                return str(activeTrade["data"]["orderid"])
         
    def getSelectedStrike(self):
        with open(constants.CURRENT_STRIKE_DATA_PATH) as f:
            activeTrade = json.load(f)
            return str(activeTrade["symbol"])

    @staticmethod    
    def getCurrentSymbol():
        try:
            with open(constants.CURRENT_STRIKE_DATA_PATH) as g:
                currentScript = json.load(g)
                return currentScript["symbol"]
        except FileNotFoundError:
            return "Clear me and put a strike!"