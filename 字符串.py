"""使用方法修改字符串的大小写"""
name='he jiaXING love lirui'
print(name.title())#方法title（）将每一个单词的首字母大写，其余字母小写
print(name.upper())#方法upper（）将每一个单词都大写
print(name.lower())#方法lower（）将每一个字母都小写

"""在字符串中使用变量"""
str1='hejiaxing'
str2='lirui'
str=f'{str1} love  {str2}'
print(str)
