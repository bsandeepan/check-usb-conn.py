# check-usb-conn.py
_License_: MIT License
---
_**Description**_: Written for unix machines, this module checks if a usb device is connected to the system or not. Works in both Python2.7 and Python 3.x environment. Note that it checks for one device at a time.  
This module is more of a plugin as of now. In future, I will add more features to it and will try to make it cross-platform compatible(Ahem!).  

### Possible Questions:
**_Question_**: Why is there no error handling methods in testing (`if __name__ == "__main__"`) section? What if the user gives incorrect device ID or multiple IDs at once?  
**_Answer_**: One of Python's core philosophy is "We are all consenting adults here." I, for one, like to treat the user as a mature adult. If you found this module by yourself, I guess that you already know what vendor_id and product_id are, how they are used, and why you may require this module for them. Therefore I see no reason to treat you as a child and add unnecessary error-handling blocks in my module.  

**_Question_**: It seems that there is no `import __future__` statement in code, so how is print() function working in Python 2.7 environment?  
**_Answer_**: It's not. In Python 2.7, the print statement is the working one and it is treating the message next to it as a tuple. More specifically, In python 2.7, print("Hello") prints the value "Hello" as a tuple value. I could have imported `__future__` but if I can make the testing code compatible with just **one hacky method**, why would I burden the module with unnecessary compatibility imports?   
