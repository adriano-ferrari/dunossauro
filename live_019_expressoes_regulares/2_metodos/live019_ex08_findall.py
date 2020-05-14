"""
FINDALL
"""
# 2_metodos$ ipython
# Python 3.7.7 (default, Apr 28 2020, 11:47:19) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: import re                                                                                                  
# 
# In [2]: 'Adriano vai pescar'                                                                                       
# Out[2]: 'Adriano vai pescar'
# 
# In [3]: re.findall('\w+', 'Adriano vai pescar')                                                                    
# Out[3]: ['Adriano', 'vai', 'pescar']
# 
# In [4]: re.findall('\w+', 'Adriano vai pescar.')                                                                   
# Out[4]: ['Adriano', 'vai', 'pescar']
# 
# In [5]: re.findall('\w+', 'Adriano, vai pescar.')                                                                  
# Out[5]: ['Adriano', 'vai', 'pescar']