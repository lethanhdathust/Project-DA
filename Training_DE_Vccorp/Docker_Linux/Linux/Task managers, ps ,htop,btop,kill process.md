### htop 
[Htop](https://htop.dev/) is a process viewer and a text mode application for system monitoring in real-time, similar to `top`. It's easy to use, and it displays a complete list of the processes that are running.

The `htop` tool is pre-installed in the distribution of Ubuntu Linux that is used to install the virtual server for this course. If `htop` isn't installed in your Linux distro, you can use the package managers in Linux to install it. (See [Part 1.3 - Install .NET Core in Linux](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/1-3-install-dotnet-core-linux) for details.)

- As with the `top` command, you can use keyboard shortcuts for several functions. For example, press **U** to select the username from a list.

![](Pasted%20image%2020231214222430.png)



- If you have to kill a process, select the process by using the arrow keys, press **F9**, and then press **Enter** to send the "terminate" signal.

![](Pasted%20image%2020231214222814.png)

### Kill process
- To kill or terminate a process, you have to send a kill signal to the process. You might recall that we used the `sudo kill -9 <PID>` command earlier to kill a process. You can also kill processes by using `top`. Press K to kill a process while `top` is running, and then type the PID of the process that you want to kill.
- The `-9` in the `kill` command is a signal or a "kill signal" in Unix-like operating systems. Specifically, `-9` refers to the `SIGKILL` signal.



#### Ps comand


![](Pasted%20image%2020231214224028.png)
⚠️upload failed, check dev console



#### Another tool like btop
![](Pasted%20image%2020231214224118.png)![](Pasted%20image%2020231214232255.png)