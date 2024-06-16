**pwd** stands for **P**rint **W**orking **D**irectory. It prints the path of the working directory, starting from the root. pwd is shell built-in command(pwd) or an actual binary(/bin/pwd). $PWD is an [environment variable](https://www.geeksforgeeks.org/environment-variables-in-linux-unix/) that stores the path of the current directory. This command has two flags.

## Syntax of `pwd` command in Linux

pwd [OPTIONS]

This command doesn’t have any arguments or options, but it can accept flags for specific behavior. 

### Flags For Specific behavior in `pwd` command in Linux.

- The “-L” flag resolves symbolic links and prints the path of the target directory.
- The default behavior of the shell built-in “pwd” is equivalent to using “pwd -L”.
- Mention the “-P” flag, which displays the actual path without resolving symbolic links.
- The default behavior of the binary “/bin/pwd” is the same as using “pwd -P”

> **pwd -L**: Prints the symbolic path. 
> 
> **pwd -P**: Prints the actual path.