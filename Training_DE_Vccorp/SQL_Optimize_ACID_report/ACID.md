**Tính nguyên tố (Atomicity).** Atomicity ensures that a series of operations within a transaction are treated as a single unit. This means that either all operations are executed successfully or none of them are. If any part of the transaction fails, the entire transaction is rolled back to its previous state.

**Tính nhất quán (Consistency).** Consistency ensures that a transaction takes the database from one valid state to another valid state, maintaining the defined rules (constraints, triggers, etc.) of the database. This means that any data written to the database must be valid according to all defined rules.

Example:
Assume a database has a constraint that a bank account balance cannot be negative. If a transaction tries to debit more money than is available in the account, it will violate this constraint and thus will not be allowed to complete.
**Tính độc lập (Isolation).** 
Isolation ensures that the operations of one transaction are invisible to other transactions until the transaction is committed. This prevents transactions from seeing intermediate states of other transactions, avoiding potential inconsistencies.

Example:
Suppose two transactions are occurring simultaneously:

Transaction A transfers $100 from Alice to Bob.
Transaction B checks the balance of Alice's account.

If isolation is maintained, Transaction B will not see Alice's balance in an inconsistent state while Transaction A is in progress.
**Tính bền vững (Durability).** D
Durability ensures that once a transaction is committed, its results are permanent and survive subsequent failures (e.g., power outages, crashes). This means the changes made by a transaction are stored in a non-volatile memory.

Example:
After a successful transfer of $100 from Alice to Bob, the changes are permanently saved in the database. Even if the system crashes immediately after the transaction is committed, the database will retain the committed transaction.