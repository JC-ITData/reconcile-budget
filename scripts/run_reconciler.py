
from budget_reconciler.bank_account_transactions.BankAccountTransaction import BankAccountTransaction
from budget_reconciler.budget_transactions.BudgetTransaction import BudgetTransaction

config_file_name = "./budget_reconciler/config.json"

bank_transactions = BankAccountTransaction(config_file_name)
data_bank_trans = bank_transactions.load_data_files()


budget_transactions = BudgetTransaction(config_file_name)
data_budget_trans = budget_transactions.load_data_files()
