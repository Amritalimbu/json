import json
a={"name":"rita","city":"bangalore","age":42}

print(json.dumps(a,separators=("@","+")))