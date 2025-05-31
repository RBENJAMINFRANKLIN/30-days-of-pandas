import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    employee = employee.sort_values(by=['salary'],ascending = False).drop_duplicates(subset = 'salary')
    if N > len(employee):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    employee1 = employee[['salary']].iloc[N-1:N]
    employee1.columns = [f'getNthHighestSalary({N})']  
    return employee1

    