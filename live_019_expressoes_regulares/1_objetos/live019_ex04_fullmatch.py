"""
FULLMATCH -> procura uma expressão exatamente igual.
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                   
# 
# In [2]: re.fullmatch('dria', 'adriano')                                                                             
# 
# In [3]: print(re.fullmatch('dria', 'adriano'))                                                                      
# None
# 
# In [4]: print(re.fullmatch('adriano', 'adriano'))                                                                   
# <re.Match object; span=(0, 7), match='adriano'>