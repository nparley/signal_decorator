signal_decorator
===============

Decorator example to catch signals in a python function

Eg:

```python
@catch_sig
def test():
    import time
    print("Waiting")
    time.sleep(60)

if __name__ == "__main__":
    test()
```

```
$ ./signal_decorator.py 
Waiting...
^CGot killed
```