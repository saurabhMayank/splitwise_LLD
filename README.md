# splitwise_LLD
LLD OF splitwise Platform

# Design Should Answer these 3 questions
- A user can see how much money he owes and lend and whom.
  - Using the show_user_balance function
  - For a specific user and group -> whole list can be shown how much credit and debit amount for other users in the group
     
- Expense can distribute unequally and equally among group members (can be selected members also. ex: 4/10 members)
    - Using the Split Factory and Split expense functionality -> Split can be done, exact, equal, percentage
    - When the expense is split then update_balance in Balance Sheet Service is called which updates the balance in the following way
         - When creating expense -> userPaidBy is also passed
         - List<Split> has the bifurcation how to split the amount among the users of the group
         - So when split_expense is called -> it updates the row of the Balance Sheet with group info, which user has paid, which user owes how much
         - Then it updates the UserBalance Model -> In that for each User and Group -> We have a column where credit/ debit info per all the users of the group mentioned
  
- Can settle the expense. modify the expense , notify the expense for every addition and editing
    - Expense can be modified using edit_expense functionality
    - Notify expense functionality is not made -> But the system is extensible to add that -> On every edit_expense/add_expense -> Observer can observe and notify users of the group
    - Observer pattern will be used in the above
    - For Settlement of expense
       - Expense can be settled using settle_expense function
       - If a user has to pay another user some amount of money in a group -> user can call settle_expense() functionality
       - settle_expense(User payingUser, User toBePaidUser, Group group)
       - This will fetch the credit amount of toBePaidUser from UserBalance model of the payingUser as it has the map of all credit and debit info
       - Then it will just update the UserBalance model of the toBePaidUser by updating its map having the credit and debit info
  
