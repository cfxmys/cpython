# 模块导入方式1
#import TemperatureConversion

#print("32摄氏度 = %.2f 华氏度" % TemperatureConversion.c2f(32))
#print("99华氏度 = %.2f 摄氏度" % TemperatureConversion.f2c(99))

# --------------------------------------------------------------

# 模块导入方式2
#from TemperatureConversion import c2f, f2c

#print("32摄氏度 = %.2f 华氏度" % c2f(32))
#print("99华氏度 = %.2f 摄氏度" % f2c(99))

# --------------------------------------------------------------

# 模块导入方式3，不推荐这种方式
#from TemperatureConversion import *

#print("32摄氏度 = %.2f 华氏度" % c2f(32))
#print("99华氏度 = %.2f 摄氏度" % f2c(99))

# --------------------------------------------------------------

# 模块导入方式4
import TemperatureConversion as tc

print("32摄氏度 = %.2f 华氏度" % tc.c2f(32))
print("99华氏度 = %.2f 摄氏度" % tc.f2c(99))
