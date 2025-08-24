from budget_reconciler.transaction.Transaction import Transaction

class BudgetTransaction(Transaction):
  def load_data_files(self, reload: bool = False) -> dict:
    return super().load_data_files('budget_data_feed', reload=reload)

