import re

print (re.search(r"([0-9])", "abc1de3f"))

# or, use re.search and on the returned match use .start()+1 for next iteration of search()
print (re.findall(r"([0-9])", "abc1de3f"))

print (re.sub("-", "", "abc-def-ghi-0123", 2))