# TP1 - Exercício 3: conversão de tipos (data_abertura, tempo_resposta_horas)
# TP1 - Exercício 6: tratamento de nulos (fillna tempo_resposta_horas, dropna ticket_id)
# TP1 - Exercício 7: remoção de duplicatas (ticket_id)
# TP1 - Exercício 8: combinação (merge) de tickets + planos + triagem do chatbot
#
# Recebe os DataFrames brutos de criar_dataframes.py e devolve o mesmo
# DataFrame consolidado usado a partir do TP2.
import numpy as np
import pandas as pd


def consolidar(tickets_df, planos_df, chatbot_df):
    df = tickets_df.copy()

    # Exercício 3: conversão de tipos
    df["data_abertura"] = pd.to_datetime(df["data_abertura"])
    df["tempo_resposta_horas"] = (
        df["tempo_resposta_horas"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .replace("", np.nan)
        .astype(float)
    )

    # Exercício 6: tratamento de nulos
    df["tempo_resposta_horas"] = df["tempo_resposta_horas"].fillna(df["tempo_resposta_horas"].mean())
    df = df.dropna(subset=["ticket_id"])

    # Exercício 7: remoção de duplicatas
    df = df.drop_duplicates(subset=["ticket_id"], keep="first")

    # Exercício 8: combinação (merge) com planos e triagem do chatbot
    df = df.merge(planos_df, on="cliente_id", how="left")
    df = df.merge(chatbot_df, on="ticket_id", how="left")

    return df.reset_index(drop=True)
