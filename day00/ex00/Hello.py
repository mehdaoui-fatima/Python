ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "Morocco!")
ft_set.remove("tutu!")
ft_set.add("Khouribga!")
ft_dict["Hello"] = "1337!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


# List: class list([iterable])
# mutable sequences, typically used to store collections of homogeneous items


# Tuple: class tuple([iterable])
# Tuples are indexed, ordred, immutable, doest support item assignment
# writing over a tuple to modify its values

# Set: class set([iterable])
# it's unordred collection of distinct hashtable element, mutable
# can be changed using methods like add() and remove()
# it has no hash value and cannot be used as
# either a dictionary key or as an element of another set

# remove(elem): remove element elem from the set.
# Raises KeyError if elem is not contained in the set
# add(elem): add element elem to the set

# dict:
# allows you to store key-value pair
# d[key] return the item of d with key key.
# Raises a KeyError if key is not in the map
# d[key] = value to Set d[key] to value.
