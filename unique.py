import json
# python_obj='{"a":3,"a":8,"a":5,"b":2,"b":7,"b":3,"c":4,"c":9}'

a= '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print("Original Python object:")
# print(python_obj)
# json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
# print(json_obj) 


# a={"x":9,"x":1,"y":4,"z":0,"z":7,"y":0}
# print("original python object:")
# print(a)
# print("\nunique key in the json object:")
b=json.loads(a)
print(b)