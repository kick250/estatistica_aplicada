# TP1 - Exercício 1: tickets_suporte
# TP1 - Exercício 2: planos_clientes e chatbot_triagem
#
# Recria, direto em memória (sem gravar csv/xlsx/json em disco), os mesmos
# DataFrames brutos que o create_data.py gera a partir do export original da
# CloudDesk, com as mesmas inconsistências (tempo_resposta_horas como texto
# com vírgula decimal, valores ausentes, duplicatas de reenvio).
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def criar_dataframes_brutos():
    rng = np.random.default_rng(42)
    n = 4000
    start_date = datetime(2026, 1, 5)

    ticket_ids = [f"TCK-{i:05d}" for i in range(1, n + 1)]
    cliente_ids = [f"CLI-{i:03d}" for i in rng.integers(1, 181, n)]
    dias_offset = np.sort(rng.integers(0, 180, n))
    datas = [(start_date + timedelta(days=int(d))).strftime("%Y-%m-%d") for d in dias_offset]
    canais = rng.choice(["email", "chat", "telefone"], size=n, p=[0.45, 0.35, 0.20])
    categorias = rng.choice(["bug", "duvida_de_uso", "cobranca", "elogio"], size=n, p=[0.35, 0.30, 0.25, 0.10])
    prioridades = rng.choice(["baixa", "media", "alta", "critica"], size=n, p=[0.30, 0.35, 0.25, 0.10])
    tempo_resposta = np.clip(rng.gamma(shape=2.0, scale=2.2, size=n), 0.2, 48)
    tempo_resposta[canais == "chat"] *= 0.6
    tempo_resolucao = np.clip(1.8 * tempo_resposta + 3 + rng.normal(0, 1.5, n), 0.5, 120)
    satisfacao = 5 - (tempo_resposta / 6) + rng.normal(0, 0.6, n)
    satisfacao[canais == "chat"] -= 0.6
    satisfacao = np.clip(np.round(satisfacao), 1, 5)

    tickets_df = pd.DataFrame({
        "ticket_id": ticket_ids,
        "cliente_id": cliente_ids,
        "data_abertura": datas,
        "canal": canais,
        "categoria": categorias,
        "prioridade": prioridades,
        "tempo_resposta_horas": tempo_resposta,
        "tempo_resolucao_horas": tempo_resolucao,
        "satisfacao_cliente": satisfacao,
    })

    # valores ausentes (como em uma exportação real)
    tickets_df.loc[rng.choice(n, size=int(n * 0.08), replace=False), "tempo_resposta_horas"] = np.nan
    tickets_df.loc[rng.choice(n, size=int(n * 0.10), replace=False), "satisfacao_cliente"] = np.nan

    # tempo_resposta_horas exportado como texto, com vírgula decimal
    def fmt_virgula(v):
        return "" if pd.isna(v) else f"{v:.2f}".replace(".", ",")

    tickets_df["tempo_resposta_horas"] = tickets_df["tempo_resposta_horas"].apply(fmt_virgula)

    # duplicatas de reenvio, anexadas ao final
    duplicatas = tickets_df.sample(frac=0.02, random_state=42)
    tickets_df = pd.concat([tickets_df, duplicatas], ignore_index=True)

    # planos_clientes
    clientes_unicos = sorted(set(cliente_ids))
    planos_df = pd.DataFrame({
        "cliente_id": clientes_unicos,
        "valor_plano": rng.choice([99.0, 199.0, 349.0, 599.0], size=len(clientes_unicos), p=[0.4, 0.3, 0.2, 0.1]),
        "segmento": rng.choice(["starter", "growth", "enterprise"], size=len(clientes_unicos), p=[0.5, 0.35, 0.15]),
    })

    # chatbot_triagem (apenas tickets abertos pelo canal chat)
    chat_ids = [tid for tid, canal in zip(ticket_ids, canais) if canal == "chat"]
    chatbot_df = pd.DataFrame([
        {
            "ticket_id": tid,
            "intencao_triagem": str(rng.choice(["duvida", "reclamacao", "solicitacao", "elogio"])),
            "confianca_bot": round(float(rng.uniform(0.55, 0.98)), 2),
        }
        for tid in chat_ids
    ])

    return tickets_df, planos_df, chatbot_df
