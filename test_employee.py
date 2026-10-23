from employee import employee_details

def test_employee_details():
    result = employee_details("Rahul", "IT", "50000")

    expected = "Name: Rahul\nEmployee ID: Emp101\nDepartment: IT|nSalary: 50000"

    assert result == expected