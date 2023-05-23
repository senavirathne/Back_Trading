import os

import websocket
import ssl
import re


class WebSocketClient:
    def __init__(self, url, headers, output_file):
        self._url = url
        self._headers = headers
        self._output_file = output_file
        self._history_data = []

    def append_to_history_data(self, line):
        self._history_data.append(line)

    def write_to_file(self):
        file = open(self._output_file, "a")
        if not os.path.exists(self._output_file) or os.path.getsize(self._output_file) == 0:
            file.write('Stock name,Stock price,Timestamp\n')
        for line in self._history_data:
            file.write(str(line))
            file.write('\n')
        file.close()

    def on_open(self, ws):
        print("Websocket opened")
        ws.send('42["s-eqbulk",["AAPL_US_EQ"]]')

    def on_message(self, ws, message):
        match = re.search(r'"eq.*","(.*?)\|(.*?)\|(.*?)"', message)
        if match:
            line = f'{match.group(1)}, {match.group(2)}, {match.group(3)}'
            print(line)
            self._history_data.append(line)

    def on_error(self, ws, error):
        # print(f"Process terminated: {error}")
        raise ValueError()

    def run(self):

        ws = websocket.WebSocketApp(self._url,
                                    header=self._headers,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_error=self.on_error)

        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
