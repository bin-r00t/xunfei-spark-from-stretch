from datetime import datetime 
from time import mktime 
from wsgiref.handlers import format_date_time

import hmac 
import hashlib
# 必须把读取config的函数单独放在一个文件，作为独立模块再导入，不然不生效
from env import get_apikey, get_api_secret
 
# 生成时间格式
def gen_date():
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return format_date_time(stamp)

def gen_protocol(version):
    s = "host: spark-api.xy-yuncom\n"
    s += f"date: {gen_date()}\n"
    s += f"GET /v{version}/chat HTTP/1.1"
    return s

# 生成auth字符串base64编码
def gen_authstring():
    pass 


if __name__ == "__main__":
  api_key = get_apikey()
  api_sec = get_api_secret()
  print(api_key, api_sec)