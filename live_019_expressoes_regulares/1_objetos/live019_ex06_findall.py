"""
FINDALL -> retorna uma lista com todos matchs encontrados.
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                   
# 
# In [2]: re.findall('a', 'adriano ferrari')                                                                          
# Out[2]: ['a', 'a', 'a']
# 
# In [3]: re.findall('a.', 'adriano ferrari')                                                                         
# Out[3]: ['ad', 'an', 'ar']
# 
# In [4]: re.findall('.a', 'adriano ferrari')                                                                         
# Out[4]: ['ia', 'ra']
# 
# In [5]: re.findall('a?', 'adriano ferrari')                                                                         
# Out[5]: ['a', '', '', '', 'a', '', '', '', '', '', '', '', 'a', '', '', '']