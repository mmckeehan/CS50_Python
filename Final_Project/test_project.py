import project

def test_confirm_csv():
    assert project.confirm_csv("TestCSV.csv") == "TestCSV.csv"
    assert project.confirm_csv("README.MD") == None


def test_function_2():
    ...


def test_function_n():
    ...