Functional API Contracts

# Group APIs
Group create_group(string name, List<User> user_list)
Group update_group(Group group, string name)
Group add_user_to_group(Group group, String name)

# Expense CRUD APIs
# User paidBy -> who paid the bill of the expense
Expense add_expense(string title, int amount, User paidBy, Group, grp)
# 4 parameters here are optional parameters
Expense edit_expense(Expense exp, string title = None, User paidBy = None, int amount = None, Group grp = None)

# Split Expense APIs
Split split_factory(ExpenseType exp_type, User user, double percentage = 0, int amount = 0)
void split_expense( Expense exp, List<Split> splits, ExpenseType expType)

# Balance Sheet and User Balance APIs
# System Facing API contract -> Not called by user
void _update_balance_sheet(Group grp, User creditUser, int amount, Map<User user, int amount>) 
void _update_user_balance(BalanceSheet balsheet, User user, Group grp)

# User Facing APIs -> Show Balance of user and settle expense
UserBalance show_user_balance(User user, Group grp)
UserBalance settle_expense(User payingUser, User toBePaidUser, Group grp)
