"""
SEARCH -> procura uma expressão em qualquer posição de uma string.
"""
# live_019_expressoes_regulares$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                   
# 
# In [2]: re.compile('Adriano')                                                                                       
# Out[2]: re.compile(r'Adriano', re.UNICODE)
# 
# In [3]: 'a' in 'adriano'                                                                                            
# Out[3]: True
# 
# In [4]: re.search('a', 'adriano')                                                                                   
# Out[4]: <re.Match object; span=(0, 1), match='a'>
# 
# In [5]: a.end()                                                                                                     
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-5-3db3de387a7f> in <module>
# ----> 1 a.end()
# 
# NameError: name 'a' is not defined
# 
# In [6]: a.end                                                                                                       
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-6-3bfb5f257538> in <module>
# ----> 1 a.end
# 
# NameError: name 'a' is not defined
# 
# In [7]: a = re.search('a', 'adriano')                                                                               
# 
# In [8]: a.end                                                                                                       
# Out[8]: <function Match.end(group=0, /)>
# 
# In [9]: a.end()                                                                                                     
# Out[9]: 1
# 
# In [10]: a.start                                                                                                    
# Out[10]: <function Match.start(group=0, /)>
# 
# In [11]: a.start()                                                                                                  
# Out[11]: 0
# 
# In [12]: a.span()                                                                                                   
# Out[12]: (0, 1)
