import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    n=2
    emp1 =  employee.sort_values(by=['salary'],ascending = False).drop_duplicates(
        subset='salary'
    )
    if 2> len(emp1):
        return pd.DataFrame({'SecondHighestSalary': [None]})
    n = emp1['salary'].iloc[n-1]
    
    return pd.DataFrame({'SecondHighestSalary': [n]})
    