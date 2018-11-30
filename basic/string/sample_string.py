string = r"C:\now\\"
print(string)

string = """你好
            我是初次学习python
            希望以后多多指教"""
print(string)

string_test_c = "测试字符串，测试字符串，中文测试"
string_test_e = "this is a string for test in english,tttttest"
string_test_e_capital = string_test_e.capitalize()

# 将字符串的第一个字符改成大写
print(string_test_e.capitalize())
# 将字符串中所有的字符改成小写
print(string_test_e_capital.casefold())
# 将字符串居中，第一个参数表示目标长度，第二个参数表示为了达到目标长度，多余的部分用第二个参数来填充
# 如果不传入第二个参数，默认为空格
print(string_test_e.center(100, '*'))
print(string_test_e.center(100))
# 将字符串左对齐，两个参数 意义同center
print(string_test_e.ljust(100, '^'))
# 将字符串右对齐，两个参数 意义同center
print(string_test_e.rjust(100, '^'))
# 获取参数1 在字符串中出现的次数；参数2 和 参数3 指定了字符串的查找范围，可以不传，如果只传入一个参数，将作为查找的开始位置
print(string_test_e.count("te", 20, 30))

