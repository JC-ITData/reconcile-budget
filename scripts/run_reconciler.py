
import budget_reconciler.bank_account_transactions.BankAccountTransaction as bank_trans


config_file_name = "./budget_reconciler/config.json"

bank_transactions = bank_trans.BankAccountTransaction(config_file_name)
data_bank_trans = bank_transactions.load_data_files()
