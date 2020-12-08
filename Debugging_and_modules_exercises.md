# What is a module?
A module is a piece of code that stands alone in its own file. It can be imported and used within other files.

# List three ways to import a module in Python.
```
- `import randome_file`
- `import randome_file as r`
- `from randome_file import *`
```

# What is the purpose of importing?
Importing allows us to make use of code and tools written by others without having to write from scratch. It is also useful when writing compartmentalized code. Each compartment is seperated and only imported when and where needed.

# List three examples when you would use the random module.
	- Picking a random number from a range
	- Executing a random selection feature
	- Implementing a coin toss
# What is an ImportError?
And ImportError occurs when there is an issue importing a module, typically occurs when there is an issue with the file path specified.

# When would using an OrderedDict be useful?
OrderedDict is useful for when there is a need to remember the exact order in which items are added to a dictionary. Otherwise, the dictionary would return its key:value pairs in an unordered manner.

# When would using a defaultdict be useful?
It is useful when trying to access a nonexistent key from a dictionary. DefaultDict creates the key in the dictionary, and assigns a previously specified default value to the key
# What is the purpose of the following code:
```
if __name__ == '__main__':
    pass
```
It allows only execution of the file the code is included in only if the file is executed directly, and refuses if the file is imported into another file.