"""
FINDITER -> retorna um um gerador com todos os matchs, cada um sendo um novo
            objeto de match.
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                   
# 
# In [2]: re.finditer('a', 'adriano ferrari')                                                                         
# Out[2]: <callable_iterator at 0x7f3025abf590>
# 
# In [3]: re.finditer('a.', 'adriano ferrari')                                                                        
# Out[3]: <callable_iterator at 0x7f30259edc50>
# 
# In [4]: re.finditer('.a', 'adriano ferrari')                                                                        
# Out[4]: <callable_iterator at 0x7f3025a0bb50>
#
# In [5]: print(re.finditer('.a', 'adriano ferrari'))                                                                 
# <callable_iterator object at 0x7f3025b38690>