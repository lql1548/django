import re
# re.findall()  返回列表，返回的结果是所有符合条件的结果
# 内容匹配
# 类型匹配   原样匹配  . \d \D \w \W [] | ()
# 长度匹配   * ? + {}
# 特殊匹配   ^ $

string = "hello world"
# 原样匹配
res = re.findall("hello",string)
print(res)