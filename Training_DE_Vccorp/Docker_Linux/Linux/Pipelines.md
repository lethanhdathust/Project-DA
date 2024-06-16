- The redirection operators are useful when save data for manual analysis or processing
- Unix provides an alternative solution fr transferring text data: a pipeline .
- The mechanism shares data between programs by passing messages. It doesn't use the file system.
- This direct connection between commands/ programs / processes allows them to operate simultaneously anh permits data to be transferred between them continously rather than having to pass it through temporary text files or through the display screen
- Pipes are unidirectional , data flows from left to right through the pipeline
#### how pipeline work
```
command_1 | command_2 | command_3 | .... | command_N
```

#### Example 
1. List all files and directories and give them as input to `grep` command using piping in Linux
```
ls | grep file.txt
```

- In this first, we are using `ls` to list all file and directories in the current directory

2. List all files and directories and give them as input to `more` commands using piping
```
ls -l | more

```

3. Sort a list of files by size using piping in Linux
```
ls -l | sort -k 5
```

---
Ex: cat test.txt | wc - l 
- `wc - l ` stand for : word count lines

Ex: cat  test.txt | grep "a"


Ex: cat test.txt | head
`head`: This command displays the beginning of a file. By default, it shows the first 10 lines of the input. So, `cat test.txt | head` displays the first 10 lines of `test.txt`.


1. **`echo "aabb" > test.txt`**:
    -> this add the new text and replace the old text
    - `echo "aabb"`: `echo` is a command used to print text to the terminal.
    - `>`: This symbol is used for output redirection. When used with `echo`, it redirects the output of `echo "aabb"` to a file named `test.txt`. In this case, it writes the string "aabb" into `test.txt`. If `test.txt` already exists, this command will overwrite its contents.
2. **`echo "cc" >> test.txt`**:
    -> it add the new text to the file
    - `echo "cc"`: Similar to the previous command, this `echo` command prints "cc" to the terminal.
    - `>>`: This symbol is used for appending output to a file. In this case, it appends the string "cc" to the end of the existing content in `test.txt`. If `test.txt` doesn't exist, it will be created.

So, after executing these commands in sequence: