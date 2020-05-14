"""
SPLIT -> dada uma expressão, fatia os dados.
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re
# 
# In [2]: 'adriano'.split(a)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-2-f9914a2e36f7> in <module>
# ----> 1 'adriano'.split(a)
# 
# NameError: name 'a' is not defined
# 
# In [3]: 'adriano'.split('a')                                                                                        
# Out[3]: ['', 'dri', 'no']
# 
# In [4]: re.split(r'a', 'adriano')                                                                                   
# Out[4]: ['', 'dri', 'no']
# 
# In [5]: re.split(r'i', 'adriano')                                                                                   
# Out[5]: ['adr', 'ano']
# 
# In [6]: re.split(r'a', 'adriano ferrari')                                                                           
# Out[6]: ['', 'dri', 'no ferr', 'ri']
# 
# In [7]: re.split(r'a|i', 'adriano ferrari')                                                                         
# Out[7]: ['', 'dr', '', 'no ferr', 'r', '']