- **mkdir** command in Linux allows the user to create directories (also referred to as folders in some operating systems). 
- This command can create multiple directories at once as well as set the permissions for the directories. It is important to note that the user executing this command must have enough permission to create a directory in the parent directory, or he/she may receive a ‘permission denied’ error.

### 1) –help:

It displays help-related information and exits.

**Syntax:**
```
**mkdir --help**
```

### 2) –version:

It displays the version number, some information regarding the license and exits.   
**Syntax:** 

```
**mkdir --version**
```

###  4) -p:

A flag which enables the command to create parent directories as necessary. If the directories exist, no error is specified.   
**Syntax:** 

```
mkdir -p [directories]
```
`
**Suppose you execute the following command –** 
```
mkdir -p first/second/third
```

If the first and second directories do not exist, due to the -p option, mkdir will create these directories for us. If we do not specify the -p option, and request the creation of directories, where parent directory doesn’t exist, we will get the following output – 

![mkdir first/second/third](https://media.geeksforgeeks.org/wp-content/uploads/20230427155930/98.webp)

```
mkdir first/second/third
```

If we specify the -p option, the directories will be created, and no error will be reported. Following is the output of one such execution. We’ve also provided the -v option, so that we can see it in action. 

![-p option](https://media.geeksforgeeks.org/wp-content/uploads/20230427163302/99.webp)

 -p option

### 5) -m:

This option is used to set the file modes, i.e. permissions, etc. for the created directories. The syntax of the mode is the same as the **chmod** command.   
**Syntax:** 

```
mkdir -m a=rwx [directories]
```