#import sys
#sys.path.append("src")
#import aula02  

from my_package import aula02

def test_columns():
    df = aula02.transform_df(aula02.load_data())
    assert list(df.columns) == ["var1", "var2", "var3", "var4", "target"]


def test_dtype():
    df = aula02.df_type(
        aula02.transform_df(aula02.load_data())
        )
    assert list(df.dtypes) == ["float", "float", "float", "float", "int"]