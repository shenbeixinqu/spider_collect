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



