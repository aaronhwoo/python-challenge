# -*- coding: utf-8 -*-
import pandas as pd

resources = "Resources/election_data.csv"

election_df = pd.read_csv(resources)

print(election_df.head(10))

print(election_df.count())

print(election_df["Candidate"].value_counts())
