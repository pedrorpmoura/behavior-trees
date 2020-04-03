import re




m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', "Malcolm Reynolds")




txt = "begin condition1 x == y y == 2 end condition1 begin condition2 x == y y == 2 end condition2"

t = re.match(r'begin (\w+) .+ end (\w+)', txt)
print(t.groups())