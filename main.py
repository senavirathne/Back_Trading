import websocket
import ssl
import re
import time

# Create a dictionary of your cookies
history_data = []
cookie = "5d60904a5b52802c63d8b5b97bf8a1ea=%2283b1d720-5562-4500-aba3-f2cc744ee4e5%22; COOKIES_CONSENT=all; LOGIN_TOKEN=eyJ0b2tlbiI6IjU2OGZlN2E0LWU5NmItNDczNi1hZDJiLTFiNWU3ZDExOTJhMyJ9; PLATFORM_LANG=ZW4%3D; LOADING_TEXT_REAL=UmVhbCBtb25leQ%3D%3D; LOADING_TEXT_DEMO=UHJhY3RpY2U%3D; _gcl_au=1.1.2082262444.1683208156; _ga=GA1.1.586487655.1683208169; _rdt_uuid=1683208168868.fa7a12f5-ccbc-4ea8-91d1-0928d63e5cae; _tt_enable_cookie=1; _ttp=95XKcwwu2YmSNM_J-7ddDkvbjSc; amp_795329_trading212.com=83b1d720-5562-4500-aba3-f2cc744ee4e5.NDUyNjMyZWMtNjI4YS00M2RjLWFjZDItY2VkNjRkNzAwMDNh..1gvtojsj1.1gvtojsqj.9.6q.73; raf5d7269aqq721cs4d68x9aq79jb5bq=eyJpbnZJZCI6IjE2WlhIS3ZWdUUifQ%3D%3D; afct=eyJjYW1wX25hbWUiOiJSRUZFUlJBTFMiLCJjYW1wX2luZm8iOiIxNlpYSEt2VnVFIn0%3D; MEDIA_SOURCE_COOKIE_KEY=Imludml0ZSI%3D; _ga_G312YS79JS=GS1.1.1683914544.9.1.1683920615.60.0.0; PLATFORM_LOADED_212=eyJudXdhbnN1bWloaXJhbkBob3RtYWlsLmNvbSI6IkRFTU8ifQ%3D%3D; TRADING212_SESSION_DEMO=ba456fa4-d067-4288-893d-c56ab1f7c50c; CUSTOMER_SESSION=ba456fa4-d067-4288-893d-c56ab1f7c50c; amp_795329=83b1d720-5562-4500-aba3-f2cc744ee4e5.NDUyNjMyZWMtNjI4YS00M2RjLWFjZDItY2VkNjRkNzAwMDNh..1h14ptvqp.1h14qcn2n.2j.1qa.1st"
# # Define the pattern to match key-value pairs
# pattern = r'(?P<key>\w+)=(?P<value>[^;]+)'
#
# # Find all matches of the pattern in the string
# matches = re.findall(pattern, cookie_string)
#
# # Create a dictionary from the matches
# cookie_dict = {match[0]: match[1] for match in matches}
#
# cookie_jar = http.cookies.SimpleCookie()
# for key, value in cookie_dict.items():
#     cookie_jar[key] = value
#
# cookie = '; '.join([f"{k}={v.value}" for k, v in cookie_jar.items()])

headers = {
    'Connection': 'Upgrade',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Upgrade': 'websocket',
    'Sec-WebSocket-Version': '13',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': cookie,
    'Sec-WebSocket-Key': '4+Ik1xfv34/LoQkmIl9RMg==',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits'
}


def on_open(ws):
    print("Websocket opened")
    # ws.send('42["subscribe","/TN",["AAPL_US_EQ"]]')
    # time.sleep(1)
    # ws.send('42["subscribe","/POS",["AAPL_US_EQ"]]')
    ws.send('42["s-eqbulk",["AAPL_US_EQ"]]')
    # ws.send('42["s-ahbulk",["AAPL_US_EQ"]]')


def on_message(ws: websocket, message):
    match = re.search(r'"eq.*","(.*?)\|(.*?)\|(.*?)"', message)

    if match:
        line = [match.group(1), match.group(2), match.group(3)]
        print(line)
        history_data.append(line)
        file.write(f'{match.group(1)},{match.group(2)},{match.group(3)}\n')
    # with open('websocket_messages.txt', 'a') as f:
    #     f.write(message + '\n')


def on_error(ws, error):
    print(f"Process terminated: {error}")


ws = websocket.WebSocketApp(
    'wss://demo.trading212.com/streaming/events/?app=WC4&appVersion=2.3.85&EIO=3&transport=websocket',
    header=headers,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error)

try:
    file = open("websocket_messages.csv", "a")
    file.write('Stock name,Stock price,Timestamp\n')
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    file.close()
    print("file connection closed: ")

except Exception as e:
    print("WebSocket connection closed: " + str(e))
