## Python File I/O

> Python provides built-in functions and methods for performing `input/output` operations on files. 

### Opening and Closing Files
Is the first step to reading or writing. This is done using the `open()` function, which takes the `filename` and the `mode`. The mode can be `'r'` for read, `'w'` for write (overwriting the file if it exists), `'a'` for appending to the file, or `'x'` for exclusive creation of a new file.

Close a file using the `close()` method. It's always a good practice to close the file after you're done, as it frees up any resources the file may have been using.

### Read Files
`read()` method, reads the entire contents of the file as a string.

> **Note**:   		  
> alt, you can use the `readline()` method to read one line of the file at a time, or the `readlines()` method to read all lines of the file at once and return them as a list of strings.

You can also use a for loop to iterate over the lines of the file, which is often more memory-efficient than reading the entire file at once.

### Write to Files
`write()` method writes a string to the file. If the file does not exist, it will be created. If the file already exists, the **write()** method will **overwrite** the existing contents of the file.

> alt, you can use the `writelines()` method to write a list of strings to the file.
