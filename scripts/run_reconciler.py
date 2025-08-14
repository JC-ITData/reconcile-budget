
import budget_reconciler.bank_account_transactions.BankAccountTransaction as bank_trans


config_file = "./budget_reconciler/config.json"

bank_transactions = bank_trans.BankAccountTransaction(config_file)
bank_transactions.load_data_files()
