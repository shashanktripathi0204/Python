```python

# Simplest form of dictionary comprehension
new_dict = {new_key : new_value for item in list}

# creating dictionary form an existing dict
new_dict = {new_key : new_value for (key, value) in dict.items() if test}
```