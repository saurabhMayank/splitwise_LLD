# Class Diagram

![splitwise_class_diag_1](https://github.com/saurabhMayank/splitwise_LLD/assets/82028762/c464ed7d-2f6f-4919-b8de-275afc179db2)
![splitwise_class_diag_2](https://github.com/saurabhMayank/splitwise_LLD/assets/82028762/5f40b5f7-8180-48bb-bed2-add29afdcffe)
![splitwise_class_diag_3](https://github.com/saurabhMayank/splitwise_LLD/assets/82028762/ea818476-7934-48b5-ab14-534f7f4e0628)



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
