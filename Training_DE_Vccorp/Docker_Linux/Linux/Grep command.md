- Grep command can be used to find or search a regular expression or a string in a text file 
- Ex : create a text file and add content to this:

```
```
```
Welcome to Linux !
Linux is a free and opensource Operating system that is mostly used by
developers and in production servers for hosting crucial components such as web
and database servers. Linux has also made a name for itself in PCs.
Beginners looking to experiment with Linux can get started with friendlier linux
distributions such as Ubuntu, Mint, Fedora and Elementary OS.

```


- To search for a string in a file

```
grep "string" file name

```

or 
```
filename grep "string"
```

Ex: 
```
grep "Linux" welcome.txt
```


- You can also specify the file path as shown below
```
grep "string" /path/to/file
```


#### Searching for a string recursively in all directories 
- Search for a string in current directory and all other subdirectories -> using the `-r ` flag :
```
grep -r "string-name" *

```

Ex: 
```
grep -r "linux" *
```

![](Pasted%20image%2020231214072808.png)


#### Ignoring case sensitivity 
- To ignore the sensitivity use th `-i` flag and execute the command
```
	grep -i "linux" welcome.txt
```

![](Pasted%20image%2020231214073638.png)

#### Count the lines where strings are matched with `-c` option


- TO count the number of lines where the a string pattern appears or resides, execute this:
```
grep -c "Linux" welcome.txt
```

#### Using grep to invert output

- The `-v` option tells grep to invert its output , meaning that instead printing matching lines, do the opposite and print all of the lines that do not match the expression .
```
grep -v "Linux" welcome.txt
```


#### Number the lines that contain the search pattern with `-n` option

- To number the lines where the string pattern is matched :

```
grep -n "Linux" welcome.txt
```

![](Pasted%20image%2020231214074200.png)