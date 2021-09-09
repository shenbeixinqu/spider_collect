import requests使用

url = "http://www.baidu.com"
response = requests使用.get(url)

# print(response.content.decode())

# 常见的响应对象和方法
print(response.url)

print(response.json)