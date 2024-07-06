my_dict = dict = {"Юрий": 2006, "Иван": 2002}
print("dict:", dict)
existing_value = my_dict["Юрий"]
print("existing_value:", existing_value)
print("Not existing value:",my_dict.get("Ксюша"))
my_dict["Алиса"] = 2007
my_dict["Оля"] = 1998
deleted_value =  my_dict.pop("Иван")
print("deleted_value:", deleted_value)
print(my_dict)
my_set = set = {1, "apple", 3.14, 1, "banana", 3.14, "apple", 3.14}
print("set:", set)
my_set.add("orange")
my_set.add(32)
my_set.remove(3.14)
print(my_set)