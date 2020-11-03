from base import BaseService
import websocket


class DataLoader(BaseService):

    @staticmethod
    def on_message(ws, message):
        DataLoader.cache['data'] = message

    @staticmethod
    def on_error(ws, error):
        print(error)

    @staticmethod
    def on_close(ws):
        print("### closed ###")

    @staticmethod
    def on_open(ws):
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

    ws = None
    cache = None

    def __init__(self, cache):
        super().__init__(cache)
        websocket.enableTrace(True)
        DataLoader.ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=btv5cpn48v6q7nvmsqs0",
                                               on_message=DataLoader.on_message,
                                               on_error=DataLoader.on_error,
                                               on_close=DataLoader.on_close,
                                               on_open=DataLoader.on_open)

    def start(self, cache):
        print('Starting service')
        DataLoader.cache = cache
        DataLoader.ws.run_forever()
