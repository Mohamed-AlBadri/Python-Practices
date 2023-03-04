def get_value(obj, key):
    keys = key.split('/')  # split the key into its parts
    for k in keys:
        obj = obj.get(k)  # get the nested object for each key
        if obj is None:
            return None  # return None if any key is not found
    return obj

object1 = {"a":{"b":{"c":"d"}}}
key1 = "a/b/c"
value1 = get_value(object1, key1)
print(value1)  # prints "d"

object2 = {"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
value2 = get_value(object2, key2)
print(value2)  # prints "a"

