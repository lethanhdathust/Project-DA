####  1: Create and close a Vim file without saving

Vim: **vim <FILE_NAME**>, where **<FILE_NAME>** represents the target file name you want to create or modify. Let's create a file named **HelloWorld.java** by typing **vim HelloWorld.java**.

|Mode|Description|
|---|---|
|Normal|Default; for navigation and simple editing|
|Insert|For explicitly inserting and modifying text|
|Command Line|For operations like saving, exiting, etc.|\

- Vim has other modes, like Visual, Select, and Ex-Mode, but Normal, Insert, and Command Line modes are good enough for us.
- ![](Pasted%20image%2020231214215353.png)

- To save and quit
```
:wq!
```


#### 2: Make and save modifications in Vim

Reopen the file by typing **vim HelloWorld.java** and pressing the **Enter** key. Insert mode is where you can make changes to a file. First, hit **Esc** to make sure you are in Normal mode, then press **i** to go into Insert mode. (Yes, that is the letter **i**.)

![](Pasted%20image%2020231214220336.png)


#### 3: Basic navigation in Vim

- Set number to show the number lines 

![](Pasted%20image%2020231214221347.png)


- You can jump the number lines with the command ; 
```
**:<LINE_NUMBER>**
```

Ex : It jump to the number line 2 in the file


![](Pasted%20image%2020231214221518.png)


#### ## 4: Basic editing in Vim

 - The _undo_ command.
 ```
 u
```

- Highlight text in Vim using the V 

. Press **v** and move your Left and Right arrow buttons to select and deselect text. This feature is also very useful when you are showing code to others and want to identify the code you want them to see.
```
v
```

- Change inner 
![[Pasted image 20231214221900.png]]


#### 5: Basic searching in Vim

```
**/<SEARCH_KEYWORD>**,
```

![[Pasted image 20231214221949.png]]



#### 6:  Use split mode in Vim

Get out of _HelloWorld.java_ and create a new file. In a terminal window, type **vim GoodBye.java** and hit **Enter** to create a new file named _GoodBye.java_.

Enter any text you want; I decided to type "Goodbye." Save the file. (Remember you can use **:x!** or **:wq** in Command Line mode.)

In Command Line mode, type **:split HelloWorld.java**, and see what happens.

![[Pasted image 20231214222041.png]]


 The **split** command created horizontally divided windows with _HelloWorld.java_ above and _GoodBye.java_ below. How can you switch between the windows? Hold **Control** (on a Mac) or **CTRL** (on a PC) then hit **ww** (i.e., **w** twice in succession).