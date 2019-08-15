from account import account
from branch import branch
from transactions import transaction

print("bc= bank creation, ac = account creation, s= search account, t= transfer")
temp = input("Enter 'bc' or 'ac' or 's' or 't': ")
if (temp == "bc"):
    branch.branch_creation()
elif (temp == "ac"):
    account.account_creation()
elif (temp == "s"):
    account.account_search()
elif (temp == "t"):
    transaction.create_transaction()