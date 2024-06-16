- In Unix operating systems, the **chmod** command is used to change the access mode of a file. The name is an abbreviation of **change mode**. 
- Which states that every file and directory has a set of permissions that control the permissions like who can read, write or execute the file. In this the permissions have three categories: read, write, and execute simultaneously represented by `r`, `w` and `x`. These letters combine together to form a specific permission for a group of users.
- The `chmod` command is used to modify this permission so that it can grant or restrict access to directories and files. Let’s have a look at the syntax and options for the `chmod` command in Linux Operating System.

**Syntax:**

```
**chmod [options] [mode] [File_name]**
```
## **“chmod” in Linux [options]**



| Options | Description                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| `-R`    | Apply the permission change recursively to all the files and directories within the specified directory.         |
| `-v`    | It will display a message for each file that is processed. while indicating the permission change that was made. |
| `-c`    | It works same as **`-v`** but in this case it only displays messages for files whose permission is changed.      |
| `-f`    | It helps in avoiding display of error messages.                                                                  |
| `-h`    | Change the permissions of symbolic links instead of the files they point to.                                     |



## “chmod” in Linux [mode]

The “mode” helps in setting new permissions that have to be applied to files or directories.

This mode can be specified in several ways, we will discuss two modes: Symbolic and Octal mode.

|Operators|Definition|
|---|---|
|`+`|Add permissions|
|`-`|Remove permissions|
|`=`|Set the permissions to the specified values|

The following letters that can be used in symbolic mode:

| Letters | Definition         |
| ------- | ------------------ |
| `r`     | Read permission    |
| `w`     | Write permission   |
| `x`     | Execute permission |



#### Examples of Using the Symbolic mode:

- Read, write and execute permissions to the file owner:

```
**chmod u+rwx [file_name]**
```

- Remove write permission for the group and others:

```
**chmod go-w [file_name]**
```

- Read and write for Owner, and Read-only for the group and other:

```
**chmod u+rw,go+r [file_name]**
```
### 2) Octal mode

It is also a method for specifying permissions. In this method we specify permission using three-digit number. Where..

-  **First digit** specify the permission for Owner.
-  **Second digit** specify the permission for Group. 
- **Third digit** specify the permission for Others. The digits 

**NOTE:** The digits are calculated by adding the values of the individual permissions.

|Value|Permission|
|---|---|
|4|Read Permission|
|2|Write Permission|
|1|Execute Permission|

#### Examples of Using the Octal mode:

Suppose if we to give read and write permission to the file Owner. Read, write and executable permission to the Group. Read-only permission to the Other. They our command would be.

  chmod 674 [file_name]

Here.

- **6** represent permission of file Owner which are **(rw).**
- **7** represent permission of Group which are **(rwx).**
- **4** represent permission of Other which is **(r).**