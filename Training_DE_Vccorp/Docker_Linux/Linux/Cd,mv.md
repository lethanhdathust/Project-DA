### Cd 
- Stand for change directory 
- ****cd**** command in Linux known as the change directory command. It is used to move efficiently from the current working directory to different directories in our System.

## ***Syntax of the `cd` command in Linux***

```
cd [directory]
```

### How to move in home directory from any location in Linux System

****`~`**** this argument is used in `cd` command to change the directory to the home directory from any location in Linux System.

****Syntax:****

cd ~

![](Pasted%20image%2020231208151841.png)

### Use of `cd “dir name”` command in Linux 

This command is used to navigate to a directory with white spaces. Instead of using double quotes we can use single quotes then also this command will work. 

```
cd "dir name"
```

Here, replace “dir name” with the directory name you want. 

****For Example:**** If we want to move to “dir name” = “My songs”. We use the following command.

```
cd "My songs"
```


![](Pasted%20image%2020231208152015.png)

---
### Mv
- mv stands for "move"
-  As its name suggests this command is used to rename file directories and move files from one location to another within a file system.
**Two Distinct Functions of `mv` Command**

- 1) Renaming a file or directory.
- 2) Moving a file or directory to another location

 ### Examples of `mv` Command

### 1) Renaming a file in Linux 

**Syntax:**

```
**mv [source_file_name(s)] [Destination_file_name]**
```

Enter your **source file name** in place of **[source_file_name(s)]** and your **destination file name** in place of **[Destination_file_name].**

For Example:

If we have a file “name = jayesh_gfg” and want to rename it to “name = geeksforgeeks”.

```
mv jayesh_gfg geeksforgeeks
```


### 2) Moving a file in Linux 

**Syntax:**

```
mv [source_file_name(s)] [Destination_path]
```

Enter your **source file name** in place of **[source_file_name(s)]** and your **destination path** in place of **[Destination_path].

```
**mv gfg_1 gfg_2 /home/jayeshkumar/jkj/**
```