def camel_to_snake(camel_case):
    snake_case = ''.join(['_' + i.lower() if i.isupper() else i for i in camel_case]).lstrip('_')
    return snake_case

def main():
    camel_case_variable = input("camelCase: ")
    snake_case_variable = camel_to_snake(camel_case_variable)
    print(f"snake_case: {snake_case_variable}")


main()
