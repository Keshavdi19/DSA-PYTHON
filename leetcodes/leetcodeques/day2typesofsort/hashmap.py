my_map = {}
my_map = {'name':'keshav','age':'21','city':'indore'}
print(my_map)
my_map['age'] = '22'
print(my_map)
my_map['college'] = 'sdbct'
print(my_map)
print(my_map["name"])     # direct access
print(my_map.get("city")) # safer way
my_map.pop("city")     # remove city
del my_map["age"]      # remove age
print(my_map)
if "name" in my_map:
    print("Name present hai")
for key, value in my_map.items():
    print(key, "->", value)
print(my_map.keys())    # dict_keys(['name', 'college'])
print(my_map.values())  # dict_values(['Keshav', 'LNCT'])
print(len(my_map))   # number of key-value pairs
my_map.clear()
print(my_map)   # {}
students = {}

# add students
students["101"] = "Aman"
students["102"] = "Neha"
students["103"] = "Ravi"

# print all
for roll, name in students.items():
    print("Roll:", roll, "Name:", name)

# access one
print("Roll 102 ka student:", students.get("102"))

# delete
students.pop("103")
print("After deletion:", students)

