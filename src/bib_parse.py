import pandas as pd

import bibtexparser as btp

def bib_to_df(bibtex_file):
    with open(bibtex_file) as f:
        dat = f.read()
    db = btp.loads(dat)
    df = pd.DataFrame(db.entries_dict)
    df = df.T.reset_index(drop=True)
    return(df)
