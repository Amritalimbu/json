import json
a='{"manpreet":1,"shivangee":2,"priyaka":3}'
b={"amrita":4}
c=json.loads(a)
c.update(b)
print(c)