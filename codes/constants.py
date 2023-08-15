TRANSACTION_ENDPOINT = "apiconnect.angelbroking.com"
MARGIN_ENDPOINT = "margincalculator.angelbroking.com"

HEADERS_PAYLOAD= "payloads/headers.json"
PLACEORDER_PAYLOAD = "payloads/placeOrder.json"
ACTIVE_TRADE_PAYLOAD = "temp/activeTrade.json"
CANCEL_ORDER_PAYLOAD = "payloads/cancelOrder.json"

CURRENT_STRIKE_DATA_PATH= "temp/currentStrike.json"

TOTP = "<get from smart api portal>"
CLIENTCODE= "<CLIENTCODE>"
PASSWORD = "<Login PIN Not Password>"

LOGIN_RESOURCE = "/rest/auth/angelbroking/user/v1/loginByPassword"
CANCEL_ORDER_RESOURCE = "/rest/secure/angelbroking/order/v1/cancelOrder"
GET_LTP_DATA_RESOURCE = "/rest/secure/angelbroking/order/v1/getLtpData"
API_VERSION_RESOURCE = "/rest/secure/angelbroking/order/v1/"
ALL_STRIKE_RESOURCE = "/OpenAPI_File/files/OpenAPIScripMaster.json"