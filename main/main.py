from utils.funcs import load_operations, get_latest_executed_operations, get_operations_details


latest_executed_operations = get_latest_executed_operations(load_operations())

for operation in latest_executed_operations:
    print(get_operations_details(operation))
