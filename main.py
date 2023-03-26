from utils.widget_output import get_operation_details
from classes.operations import Operations

def main():
    user_operations = Operations('operations.json')
    get_operation_details(user_operations.get_last_ex(5))

if __name__ == '__main__':
    main()
