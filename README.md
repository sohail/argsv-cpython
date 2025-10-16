**argsv-cpython**    
_README, last updated on :- 17th of October, 2025_

argsv for CPython(a CPython module). An effort to process the command line arguments with ease and style.  
---

"Command-line options represent the \"face\" of the program, and tools for options parsing should be convenient and easy to use.". C/C++ Users Journal November, 2004.

This argsv-cpython is capable of handling short and long commands. It is capable of handling multiple instances of same short or long command. argsv-cpython allows many command names for the same command e.g "?,/?,h,-h,help,--help"(This comma delimited list represents few names of the one single command). argsv-cpython module allows the use of funtions print, str and len on its type instances. 

Please Note: This module is compatible with Python versions earlier than 3.0. For newer versions, use the implementation in the **argsv-cpython-Python3.9** folder, which has been tested and confirmed to work with Python 3.8, 3.9.0-alpha1, and 3.15.0a0.

Example Application.
-----------------------
Few \"example applications\"(**test_argsv.py**, **regedit.py**) are part of the committed source code, use it as a usage guide and to test the smarts of argsv-cpython module.


```python

import sys

try:
    import argsv

    # argsv module allows several names of one single command
    # Here we are asking argsv to process three different commands
    args=argsv.argsv(sys.argv, "?,-?,/?,h,-h,help,--help#d,-d,dir,--dir#v,version")
    
    # str(args) throws TypeError exception when no command line arguments
    # are given at command line of this application
    print ("All commands at CL are --> " + str(args))

except (ImportError, MemoryError, TypeError) as e:
   print (e)        

```

```Python 
import sys

try:    
    import cbow, argsv

    print (cbow.add(2, 3))

    # argsv module allows several names of one single command
    # Here we are asking argsv to process three different commands
    args=argsv.argsv(sys.argv, "?,-?,/?,h,-h,help,--help#v,version#lr,--lr#rs,--rs#ns,--ns#w1#w2#input#output#e,--e#corpus,--corpus")

    lr_arg = None    
    ns_arg = None
    rs_arg = None
    e_arg = None
    fn_arg = None

    for arg in args:
        if arg[b"--lr"]:           
            lr_arg = arg[b"--lr"](1)[1:]                        
        elif arg[b"rs"]:
            rs_arg = arg[b"rs"](1)[1:]
        elif arg[b"--ns"]:
            ns_arg = arg[b"ns"](1)[1:] 
        elif arg[b"e"]:
            e_arg = arg[b"--e"](1)[1:]
        elif arg[b"--corpus"]:
            fn_arg = arg[b"corpus"](1)[1:]

    if lr_arg == None or not len(lr_arg) > 0:        
       raise ValueError("Learning rate is not provided. Please specify a valid learning rate using the 'lr' argument (e.g., 'lr 0.01').")       
    
    if ns_arg == None or not (len(ns_arg) > 0):
       raise ValueError("Negative sample number is not provided. Please specify a valid number of negative samples using the 'ns' argument (e.g., 'ns 0').")

    if rs_arg == None or not len(rs_arg) > 0:
       raise ValueError("Regularization strength is not provided. Please specify a valid regularization strength using the 'rs' argument (e.g., 'rs 0').")
 
    if e_arg == None or not len(e_arg) > 0:
        raise ValueError("Number of epochs is not provided. Please specify a valid number of epochs using the 'e' argument (e.g., 'e 1').")
    
    if fn_arg == None or not len(fn_arg) > 0:
        raise ValueError("Name of the file containing training and validation data is not provided. Please provide the name of valid corpus file using the 'corpus' argument (e.g., 'corpus vocab.txt')")
    
    if int(e_arg[0]) < 0:
        raise ValueError("Number of epochs must be non-negative (e.g., 'e 1').")
    
    if int(ns_arg[0]) < 0:
        raise ValueError("Number of negative samples must be non-negative (e.g., 'ns 5').")

    cbow.start_training(float(lr_arg[0]), float(rs_arg[0]), int(ns_arg[0]), int(e_arg[0]), fn_arg[0])

    print ("Training Done!")    

except (ImportError, MemoryError, TypeError, ValueError, IndexError, RuntimeError) as e:
    print (e) 
```

