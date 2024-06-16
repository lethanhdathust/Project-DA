It is the complementary of [Tail](https://www.geeksforgeeks.org/tail-command-linux-examples/) command. The head command, as the name implies, print the top N number of data of the given input. By default, it prints the first 10 lines of the specified files. If more than one file name is provided then data from each file is preceded by its file name. 

**Syntax:**   
 

```
head [OPTION]... [FILE]...
```

Let us consider two files having name **state.txt** and **capital.txt** contains all the names of the Indian states and capitals respectively.
  
![](https://media.geeksforgeeks.org/wp-content/uploads/head.png)

**1. -n num:** Prints the first ‘num’ lines instead of first 10 lines. **num** is mandatory to be specified in command otherwise it displays an error.   
 

**$ head -n 5 state.txt**
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh

**2. -c num:** Prints the first ‘num’ bytes from the file specified. Newline count as a single character, so if head prints out a newline, it will count it as a byte. **num** is mandatory to be specified in command otherwise displays an error.   
 

```
**$ head -c 6 state.txt**
Andhra
```

**3. -q:** It is used if more than 1 file is given. Because of this command, data from each file is not precedes by its file name.   
 

```
**Without using -q option**
**$ head state.txt capital.txt**
==> state.txt <==
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir

==> capital.txt <==
Hyderabad
Itanagar
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh
Shimla
Srinagar
```

`With using -q option

```
**$ head -q  state.txt capital.txt**
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir
Hyderabad
Itanagar
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh
Shimla
Srinagar
```
`
**4. -v:** By using this option, data from the specified file is always preceded by its file name.   
 
```
**$ head -v state.txt**
==> state.txt <==
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir
```