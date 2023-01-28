#Reid Witte
#Using w3schools as a reference

import BankAccount

BA = BankAccount.BankAccount("Reid", 4.00)

BA.deposit(4.50)
BA.withdraw(2.25)

print(BA.get_balance())