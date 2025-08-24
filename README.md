# reconcile-budget

This code is used when you have a budget app. At times, the balances and transactions can get out of synch with actual account balances and transactions. This is used to reconcile the differences between what is actually in your credit card accounts and what is in the budget app.

The app assumes 1 or more bank account(s) and 1 budget.

## Instructions
1. Export transactions from your bank accounts and budget application to csv format
2. Create your schema files 
- Rename the folder "schema_files_TEMPLATE" to "schema_files"
- Create the schema files for the budget file each bank account. Use the samples provided to identify the structure of the schema files.
3. Create your config file
- Rename the file config_TEMPLATE.json to config.json
- Update the paths to point to the location of the data files created in step 1. 


## Outstanding 
load_data_files parameter reload
match budget data and bank transactions

