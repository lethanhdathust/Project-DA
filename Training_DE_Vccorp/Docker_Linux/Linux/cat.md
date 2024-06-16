### Cat (concatenate)

- Cat(concatenate) command is very frequently used in Linux. It reads data from the file and gives its content as output. It helps us to create, view, and concatenate files. So let us see some frequently used cat commands.

1) To view a single file

**Syntax:** 

```
cat file_name

```

**2) To view multiple files** 

**Syntax:**

```
cat file_name1 file_name2
```

**Example:** If we have two files , file1 and file2.

```
cat file1 file2
```


**3) To view contents of a file preceding with line numbers.** 

**Syntax:**

```
cat -n file_name
```

**Example:** If our file_name is file2.

```
cat -n file2
```


**4) Create a file and add content** 

**Syntax:**

```
cat > newfile_name
```

**Example:** If we want to create a newfile_name = jayesh1.

```
cat > jayesh1
```


**5) Copy the contents of one file to another file.** 

**Syntax:**

```
$cat [filename-whose-contents-is-to-be-copied] > [destination-filename]
```

Output  

The content will be copied in destination file

**6) Cat command can suppress repeated empty lines in output** 

**Syntax:**

```
cat -s file_name
```

Output  

Will suppress repeated empty lines in output

**7) Cat command can append the contents of one file to the end of another file.** 

**Syntax:** 

cat file_name1 >> file_name2

**Example:**

cat file1 >> file2

![](https://media.geeksforgeeks.org/wp-content/uploads/20230620140311/313.png)

**8) Cat command can display content in reverse order using tac command.** 

**Syntax:**

tac file_name

**Example:**

tac file2

![tac file2](https://media.geeksforgeeks.org/wp-content/uploads/20230620140616/314.png)

tac file2

**9) Cat command can highlight the end of line.** 

**Syntax:** 

cat -E "filename"

**Output:** 

Will highlight the end of line

**10) If you want to use the -v, -E and -T option together, then instead of writing -vET in the command, you can just use the -A command line option.** 

**Syntax:**

cat -A  "filename"

**11) Cat command to open dashed files.** 

**Syntax:**

cat -- "-dashfile"

**Output:** 

Will display the content of -dashfile

**12) Cat command if the file has a lot of content and can’t fit in the terminal.** 

**Syntax:** 

cat "filename" | more

**Output:**

Will show that much content, which could fit in terminal and will ask to show more.

**13) Cat command to merge the contents of multiple files.** 

**Syntax:** 

cat "filename1" "filename2" "filename3" > "merged_filename"

**Output:** 

Will merge the contents of file in respective order and will insert that content in "merged_filename".

**14) Cat command to display the content of all text files in the folder.** 

**Syntax:**

cat *.txt

**Output:**  

Will show the content of all text files present in the folder.

**15) Cat command to write in an already existing file.** 

**Syntax:**

cat >> geeks.txt
The newly added text.

**Output:**

Will append the text "The newly added text." to the end of the file.