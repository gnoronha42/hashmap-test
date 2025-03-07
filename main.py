import re

enderecos = [
    "100-2, Rua das Flores - Centro",
    "Rua das Árvores 25. Bairro Verde",
    "Avenida Brasil 34. Vila Nova",
    "400 Rua Sem Formato-Jardim Azul",
    "Avenida Paulista #1000 - Bela Vista",
    "R. XV de Novembro, 45. Centro",
    "25 Rua Sem Padrão, Bairro Perdido",
    "Rua do Comércio.1000.Centro",
    "500 Rua dos Testes, Bairro de Exemplo",
    "Rua das Palmeiras 200 - Jardim das Árvores",
    "Nº 10 - Rua Sem Nome. Sem Bairro",
    "Avenida das Nações, 1500. Vila Global",
    "Rua Aleatória - Nº 90. Bairro Desconhecido",
    "R. Sem Fim, nº 77, Bairro Distante",
    "30# Rua com Símbolos - Bairro Diferente",
    "Praça da Liberdade 250. Bairro Antigo",
    "Rua da Esperança - 300. Centro",
    "Avenida dos Exageros nº 4000. Bairro Alto",
    "Beco do Mistério, 12. Bairro Escuro",
    "Estrada Velha - 500, Bairro Antigo"
]

def padronizar_endereco(endereco: str) -> str:
    padrao = r"(?i)(?:nº\s*|#|^|\s*)(\d+[\-\d]*)[\s,.-]*([\w\s]+?)[\s,.-]+([\w\s]+)$"
    match = re.search(padrao, endereco)
    if match:
        numero, rua, bairro = match.groups()
        return f"{numero.strip()}, {rua.strip()}, {bairro.strip()}"
    return f"Formato não reconhecido: {endereco}"

enderecos_padronizados = [padronizar_endereco(endereco) for endereco in enderecos]

for endereco in enderecos_padronizados:
    print(endereco)
