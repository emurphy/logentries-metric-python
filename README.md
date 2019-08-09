# logentries-metric

A simple python script to reproduce the logentries.metrics.py error:

$ python measure_me.py
> Traceback (most recent call last):
  File "/work/logentries-metric/measure_me.py", line 1, in <module>
    from logentries import metrics
  File "/Users/.local/share/virtualenvs/logentries-metric-yrunR7wA/lib/python3.7/site-packages/logentries/metrics.py", line 58
    return f(*args, **kwargs)                
>                                            ^  
> TabError: inconsistent use of tabs and spaces in indentation


## Environment

The error happens with:
 - MacOS Mojave 10.14.5
 - python 3.7.1

## Steps to reproduce

Recommend installing pipenv and then:

```bash
pipenv --python 3.7.1 install
pipenv shell
python measure_me.py
```

