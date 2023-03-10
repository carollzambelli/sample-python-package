"""Este script tem como finalidade baixar a base de dados iris realizar alguns tratamentos e salvar a base em csv"""
import pandas as pd
from sklearn.datasets import load_iris


def load_data():
    """
    Description: Função para baixar os dados do iris dataset
    """
    return load_iris()

def transform_df(data):
    """
    Description: Função para transformar em dataframe e nomeia as colunas
    Arguments: dataset
    """
    data_frame = pd.DataFrame(data['data'], columns=["var1", "var2", "var3", "var4"])
    data_frame['target'] = data['target']
    return data_frame


def df_type(data_frame):
    """
    Description: Função para tipar os dados do iris dataset
    Arguments: dataset
    """
    type_lst = ["float", "float", "float", "float", "int"]
    for i,j in enumerate(data_frame.columns):
        data_frame[j] = data_frame[j].astype(type_lst[i])
    return data_frame

def save_df(data_frame, name):
    """
    Description: Função para salvar os dados tratados
    Arguments: dataset
    """
    data_frame.to_csv(name, index=False)


def main():
    """
    Função main
    """
    data_frame = df_type(
        transform_df(load_data())
        )
    save_df(data_frame, "iris.csv")


if __name__ == "__main__":
    main()

