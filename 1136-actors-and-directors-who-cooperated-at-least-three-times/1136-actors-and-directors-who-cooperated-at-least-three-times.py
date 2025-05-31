import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    ac = actor_director.groupby(['actor_id','director_id'])[['timestamp']].nunique().reset_index()
    #ac = ac.loc([])
    ac = ac[ac['timestamp']>=3]
    ac = ac[['actor_id','director_id']]
    return ac