# You are an object...

# Create a python (.py) file named object.py inside your folder. Inside this file solve the following problem: Create a dictionary (aka an object) that represents yourself. Assign ten attributes about yourself to this object. Use a loop to list all of these attributes (and the keys that they are associated with). Print both the key and value of the object in a string like this, replacing the quoted values for each key and value pair appropriately: "'Your name' has 'key' of 'value'".

attribute_dict = { 'attr1' : 'nice', 'attr2' : 'funny', 'attr3' : 'confused', 'attr4' : 'coder', 'attr5' : 'slow'}

for i in attribute_dict:
	print("Hailey has " + i + " of " + attribute_dict[i])