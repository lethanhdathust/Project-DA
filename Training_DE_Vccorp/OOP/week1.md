  ## Exercise 1.1:
1. Description
- We have three type of customers : non-registered customer , registered customer and manager . Each Customer can orders 0 or many orders. ALl customer have buyOrder() function, Only User can use generateReceipt() function.
- Order class have three attributes and two function to calculate the Total and Tax.
2. Explain the way i apply OOP in my project
- **Inheritance**: Because i have three class have the same attributes and method , so i define a base class called  Customer for all type of customers to inherit.Another interface i define to inherit is User , because Register Customer and Manager have the same method (generateReceipt())  
- **Abstraction**: I only focus on the function of customer, i do not focus detail on how the function implement .Besides, All customer have the same method buyOrder() but different implementation
Another way I obtain the abstraction is using interface (interface User), which support multiple inherit (registeredCustomer and Manager inherit from both Customer and User).
- **Polymorphism** : All the customer perform the buyOrder() function in different ways by override that function, it ís called Runtime Polymorphism.
- **Encapsulation** : I use private to obtain the Encapsulation , which means they can only be accessed within the class.Besides,Public methods  getters and setters are defined, which are used to retrieve and modify the values of the variables.
- **Static**: I use numberOfOrder attribute to share the variable among all instances of the Manager class. So when i buy a new order, the variable will  auto increase 
Ex
- Class diagram : 
- ![Alt](class_diagram_3.drawio.png)

## Exercise 1.2:
  - Here are the list of function to interact with file and folder:


            System.out.println("\t\t*******************************************");
            System.out.println("\n\nPress 1 : To write text file ");
            System.out.println("Press 2 : To read text file");
            System.out.println("Press 3 : To write binary file ");
            System.out.println("Press 4 : To Read binary file");
            System.out.println("Press 5 : To Read file info");
            System.out.println("Press 6 : To get Current Project Path");
            System.out.println("Press 7 : To create Folder");
            System.out.println("Press 8 : To listed The File And Folder In A Folder");

            System.out.println("Press 10 : To  exit ");

