"""
MATCH -> procura uma expressão no início de uma string (startswith).
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                   
# 
# In [2]: re.match('o', 'adriano')                                                                                    
# 
# In [3]: type(re.match('o', 'adriano'))                                                                              
# Out[3]: NoneType
# 
# In [4]: re.match('a', 'adriano')                                                                                    
# Out[4]: <re.Match object; span=(0, 1), match='a'>
