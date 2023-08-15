import http.client
import json
import ssl
import sys
import datetime
import constants
import ijson


class LoadSymbol:

    def __init__(self):
        self.connection = http.client.HTTPSConnection(constants.MARGIN_ENDPOINT, context = ssl._create_unverified_context())

    def downloadStrikeData(self, strike):
        today = datetime.date.today()
        days_until_expiry = (3 - today.weekday()) % 7
        expiry = (today + datetime.timedelta(days=days_until_expiry)).strftime("%d%b%y").upper()
        symbol = "NIFTY" + expiry+ str(strike).lstrip().rstrip()
        self.connection.request("GET", constants.ALL_STRIKE_RESOURCE , '', json.loads(open(constants.HEADERS_PAYLOAD).read()))
        datas= json.loads(self.connection.getresponse().read().decode("utf-8"))
        for data in datas:
            if (data["symbol"] == str(symbol)):
                with open(constants.CURRENT_STRIKE_DATA_PATH, 'w') as json_file:
                    json_file.write(json.dumps(data))
                return "SELECTED STRIKE: "+ data["symbol"]
    