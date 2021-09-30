## requests

### 响应对象

```python
respose = requests.get(url)
print(response.text)  //内容为str类型对象 出现乱码的现象
print(response.content.decode())
```

## etree与xpath集合使用

```shell
res=requests.get(url,headers=headers)
res.encoding = 'utf-8'
selector = etree.HTML(res.text)
xpath_reg = "//div/*/text()"
results = selector.xpath(xpath_reg)
content = results[0]
```

## xpath

**常用规则**

```shell
/从当前节点选取直接子节点
//从当前节点选取子孙节点
.选取当前节点
..选取当前节点的父节点
@选取属性

eg
//title[@lang=’eng’]
它就代表选择所有名称为 title，同时属性 lang 的值为 eng 的节点。
```

**属性匹配**

```shell
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
在这里我们通过加入 [@class="item-0"] 就限制了节点的 class 属性为 item-0，而 HTML 文本中符合条件的 li 节点有两个，所以返回结果应该返回两个匹配到的元素，
```

**文本获取**

```shell
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
```

**属性获取**

```shell
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
```

**属性多值匹配**

```shell
属性有多个值时,如class="li li-first" 用上面的属性匹配就无法获得结果了
这时需要使用contains（）函数
from lxml import etree
text = '''
<li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

```

**多属性匹配**

```shell
有时我们可能需要多个属性才能确定一个节点,这时就需要同时匹配多个属性才可以
这时需要使用and来连接
from lxml import etree
text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)    ['first item']
```

**按序选择**

```shell
匹配了多个节点 我们只想要其中的某个节点
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

第一次选择我们选取了第一个 li 节点，中括号中传入数字1即可，注意这里和代码中不同，序号是以 1 开头的，不是 0 开头的。

第二次选择我们选取了最后一个 li 节点，中括号中传入 last() 即可，返回的便是最后一个 li 节点。

第三次选择我们选取了位置小于 3 的 li 节点，也就是位置序号为 1 和 2 的节点，得到的结果就是前 2 个 li 节点。

第四次选择我们选取了倒数第三个 li 节点，中括号中传入 last()-2即可，因为 last() 是最后一个，所以 last()-2 就是倒数第三个。

运行结果如下：
['first item']
['fifth item']
['first item', 'second item']
['third item']
```

## re

| \w   | 匹配字母数字及下划线                  |
| ---- | ------------------------------------- |
| \W   | 匹配非字母数字及下划线                |
| \s   | 匹配任意空白字符  等价于 \t \n \r  \f |
| \S   | 匹配任意非空字符                      |
| \d   | 匹配任意数字,等价于[0-9]              |
| \D   | 匹配任意非数字                        |
| *    | 匹配0个或多个                         |
| +    | 匹配1个或多个                         |
| ?    | 匹配0个或1个                          |



| 模式    | 匹配方式                              | 返回结果                       |
| ------- | ------------------------------------- | ------------------------------ |
| match   | 只从字符串起始位置进行匹配            | None或者起始位置匹配成功的字符 |
| search  | 整个字符串,并返回第一个符合要求的匹配 | 第一个匹配成功的字符           |
| findall | 满足要求的所有匹配                    | 列表形式返回                   |

**re.match**

```shell
re.match(a, b) 
a放正则表达式,b放要匹配的字符串,如果第一个字符不符合就返回none

test_str = 'www.weather.com'
pattern = r'w'
rm1 = re.match(pattern, test_str)
print(rm1)

匹配结果.group()  从1开始,对应匹配到的结果
```

**re.search**

```shell
在字符中查找匹配 查找到第一处立刻结束
用法同 re.match
```

**re.findall**

```shell
遍历字符串进行匹配,返回一个list格式  没匹配到结果为[]
```

**re.I 忽略大小写匹配**

```shell
test_str = '结果R'
pattern = r'结果r'
rm = re.findall(pattern, test_str, re.I)
print(rm) 	// ['结果R']
```

**re.A 匹配ASCII**

```shell
test_str = 'a结果b显示c'
pattern = r'\w+'
rm1 = re.findall(pattern, test_str)
rm2 = re.findall(pattern, test_str, re.A)

print(rm1)  //['a结果b显示c']
print(rm2)  // ['a', 'b', 'c']
```

**re.S 匹配换行符**

```shell
test_str = '结果\n显示'
pattern = r'.*'
rm1 = re.findall(pattern, test_str)
rm2 = re.findall(pattern, test_str, re.S)

print(rm1) ['结果', '', '显示', '']
print(rm2) ['结果\n显示', '']
```

**re.M 匹配多行模式**

```shell
当某字符中有换行符时,默认情况下是不支持换行符特性的
test_str = '结果\n显示'
pattern = r'^显示'
rm1 = re.findall(pattern, test_str)
rm2 = re.findall(pattern, test_str, re.M)

print(rm1) // []
print(rm2) // ['显示']
```

**re.sub()**

```shell
替换字符串中的匹配项

phone = "2004-959-559"

num = re.sub(r'\D', '', phone)
print(num)  // 2004959559
```

**re.compile**

```shell
编译正则表达式 供match()和search()函数使用
pattern = re.compile(r'\d+')
m = pattern.match("one12twothree34four")
print(m)   // None
m = pattern.match("one12twothree34four". 3, 10)
print(m) // 匹配对象
```



