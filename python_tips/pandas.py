# Some Python tips for reference

# Split string into several columns in pandas dataframe
import pandas as pd
s = pd.Series(['aa-123', 'ff-ds-ds', 'zzz-42', 'xx'])
s.str.split("-", 1)
"""
[aa, 123]
[ff, ds-ds]
[zzz, 42]
[xx]
"""
s.str.split("-", 1, expand = True)
"""
0  |  1
-------
aa | 123
ff | ds-ds
zzz| 42
xx | None
"""