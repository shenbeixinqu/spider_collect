import re

test_str = '结果\n显示'
pattern = r'^显示'
rm1 = re.findall(pattern, test_str)
rm2 = re.findall(pattern, test_str, re.M)

print(rm1)
print(rm2)