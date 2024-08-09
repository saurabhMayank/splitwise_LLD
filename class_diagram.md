# Class Diagram
![splitwise_1](https://github.com/user-attachments/assets/0bd844d3-02f9-4e4e-815d-91ff4dcb17af)
![splitwise_2](https://github.com/user-attachments/assets/17893ea2-a67c-4850-aa22-fc4e59855606)
![splitwise_3](https://github.com/user-attachments/assets/1cd1663c-0755-493c-baf7-deae3215c4e9)







# Explanation of Class Diagram -> Flow of the System
1. Splitwise Handler will first create User -> User service
2. Then a group will be created -> Group Service
3. After that the User can add others users to the group -> Group Service
4. User can add/ Edit Expense in a group -> Expense Service (Please see the API contract file for exact definition of the API)
5. User can split the Expense using Expense Service (Please see the API contract file for exact definition of the API)
6. User can Settle the Expense using Expense Service
7. User can see the current balance per group using the -> BalanceSheet Service

# SWE Principles and Patterns
1. SOLID principles used -> Single Responsibility Principle of classes, Interface for Data Models
2. Composition Preferred over inheritance -> Expense Service and Split Expense Algorithm Classes (Percentage Expense, Exact Expense, Equal Expense)
3. Strategy Design pattern used for Different Strategies of calculating expense
4. Factory Design Pattern Used for Creating a Split based on Expense Type and returing Split instance
