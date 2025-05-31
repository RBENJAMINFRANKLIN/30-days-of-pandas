import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    n=2
    emp1 =  employee['salary'].sort_values(ascending = False).drop_duplicates(
        
    )
    if 2> len(emp1):
        return pd.DataFrame({'SecondHighestSalary': [None]})
    n = emp1.iloc[n-1]
    
    return pd.DataFrame({'SecondHighestSalary': [n]})
    