url = 'wss://demo.trading212.com/streaming/events/?app=WC4&appVersion=2.3.85&EIO=3&transport=websocket'
cookie = "5d60904a5b52802c63d8b5b97bf8a1ea=%2283b1d720-5562-4500-aba3-f2cc744ee4e5%22; COOKIES_CONSENT=all; LOGIN_TOKEN=eyJ0b2tlbiI6IjU2OGZlN2E0LWU5NmItNDczNi1hZDJiLTFiNWU3ZDExOTJhMyJ9; PLATFORM_LANG=ZW4%3D; LOADING_TEXT_REAL=UmVhbCBtb25leQ%3D%3D; LOADING_TEXT_DEMO=UHJhY3RpY2U%3D; _gcl_au=1.1.2082262444.1683208156; _ga=GA1.1.586487655.1683208169; _rdt_uuid=1683208168868.fa7a12f5-ccbc-4ea8-91d1-0928d63e5cae; _tt_enable_cookie=1; _ttp=95XKcwwu2YmSNM_J-7ddDkvbjSc; amp_795329_trading212.com=83b1d720-5562-4500-aba3-f2cc744ee4e5.NDUyNjMyZWMtNjI4YS00M2RjLWFjZDItY2VkNjRkNzAwMDNh..1gvtojsj1.1gvtojsqj.9.6q.73; raf5d7269aqq721cs4d68x9aq79jb5bq=eyJpbnZJZCI6IjE2WlhIS3ZWdUUifQ%3D%3D; afct=eyJjYW1wX25hbWUiOiJSRUZFUlJBTFMiLCJjYW1wX2luZm8iOiIxNlpYSEt2VnVFIn0%3D; MEDIA_SOURCE_COOKIE_KEY=Imludml0ZSI%3D; _ga_G312YS79JS=GS1.1.1683914544.9.1.1683920615.60.0.0; PLATFORM_LOADED_212=eyJudXdhbnN1bWloaXJhbkBob3RtYWlsLmNvbSI6IkRFTU8ifQ%3D%3D; TRADING212_SESSION_DEMO=ba456fa4-d067-4288-893d-c56ab1f7c50c; CUSTOMER_SESSION=ba456fa4-d067-4288-893d-c56ab1f7c50c; amp_795329=83b1d720-5562-4500-aba3-f2cc744ee4e5.NDUyNjMyZWMtNjI4YS00M2RjLWFjZDItY2VkNjRkNzAwMDNh..1h14ptvqp.1h14qcn2n.2j.1qa.1st"
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
output_file = "websocket_messages.csv"
