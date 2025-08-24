from budget_reconciler.transactions.Transaction import Transaction

class BankAccountTransaction(Transaction):
  def load_data_files(self, reload: bool = False) -> dict:
    return super().load_data_files('bank_data_feeds', reload=reload)


