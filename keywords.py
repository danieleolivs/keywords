import csv
import re
import json
import sys
from google.colab import files

def extrair_frases(ementa_texto):
   
    if not isinstance(ementa_texto, str):
        return []

    ementa_limpa = ementa_texto.replace('\n', ' ').replace(';', '.')
    ementa_limpa = re.sub(r'[ºª§?]', '', ementa_limpa)
    ementa_limpa = re.sub(r'\s+', ' ', ementa_limpa).strip()

    partes = re.split(r'\s*[\.-]\s*', ementa_limpa)
    frases_validas = []

    VERBOS_COMUNS = {
        'é', 'foi', 'será', 'seja', 'sendo', 'são', 'eram', 'serão', 'sejam', 'ser',
        'está', 'esteja', 'estava', 'estão', 'estavam', 'estar', 'há', 'houve',
        'haverá', 'haja', 'haver', 'tem', 'tinha', 'terá', 'tenha', 'têm',
        'tinham', 'ter', 'pode', 'pôde', 'poderá', 'possa', 'podem', 'poder',
        'deve', 'deva', 'devem', 'dever', 'trata', 'tratam', 'tratou', 'tratar',
        'configura', 'configurou', 'configurar', 'viola', 'violou', 'julga',
        'julgou', 'julgar', 'julgado', 'nega', 'negou', 'negar', 'negado', 'dá',
        'deu', 'dar', 'dado', 'provê', 'proveu', 'prover', 'provido', 'conhece',
        'conheceu', 'conhecer', 'conhecido', 'acolhe', 'acolheu', 'acolhido',
        'rejeita', 'rejeitou', 'rejeitado', 'determina', 'determinou'
    }

    FRAGMENT_STARTERS = re.compile(
        r'^(Hipótese|Caso|Momento|Oportunidade) em que'
        r'|^(Razão|Motivo) pela qual'
        r'|^(Ainda|Mesmo|Posto) que',
        re.IGNORECASE
    )

    PADROES_RUIDO_GERAL = re.compile(
        r'\b(art|lei|fls|inc|cf|stj|stf|nº|rel|proc|junior|filho|neto|magalhães)\b|'
        r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b|'
        r',\s*j$|'
        r'[\/\\_"\']',
        re.IGNORECASE
    )

    PADROES_FIM_FRAGMENTADO = re.compile(
        r'.*,\s+\w+$|' 
        r'.*[\'ê]$|' 
        r'.*\s(sendo|tendo|havendo|podendo|devendo|considerando|confirmando|julgando|julgadocomentando|tratando|vista|assentou|remunerando|determina|pronuncia|tem)$',
        re.IGNORECASE
    )


    for parte in partes:
        frase = parte.strip(' .,:;"\'')
        if not frase or len(frase) < 10:
            continue

        frase_sem_marcador = re.sub(r'^[0-9a-zA-Z][\.\)]\s*', '', frase).strip()
        if not frase_sem_marcador:
            continue

        palavras = frase_sem_marcador.split()
        if not (2 <= len(palavras) <= 7):
            continue

        if FRAGMENT_STARTERS.search(frase_sem_marcador):
            continue

        if PADROES_FIM_FRAGMENTADO.match(frase_sem_marcador):
            continue
            
        if not frase_sem_marcador.isupper() and PADROES_RUIDO_GERAL.search(frase_sem_marcador):
            continue

        if not frase_sem_marcador.isupper():
            if not any(palavra.lower() in VERBOS_COMUNS for palavra in palavras):
                continue
        
        if '(' in frase_sem_marcador or ')' in frase_sem_marcador or frase_sem_marcador.count(',') > 1:
            continue
        if re.search(r'\d', frase_sem_marcador) and not re.search(r'\bICMS\b', frase_sem_marcador, re.I):
            continue

        frases_validas.append(frase_sem_marcador)

    return list(dict.fromkeys(frases_validas))

uploaded = files.upload()
csv_input_path = next(iter(uploaded))
resultados = {}

try:
    with open(csv_input_path, mode='r', encoding='utf-8-sig', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        if 'id' not in reader.fieldnames or 'ementa' not in reader.fieldnames:
            raise ValueError("Colunas 'id' ou 'ementa' não encontradas no CSV.")

        count = 0
        total_linhas = 0
        for i, row in enumerate(reader):
            total_linhas = i + 1
            ementa = row.get('ementa', '')
            row_id = row.get('id', f'linha_{total_linhas}')

            if ementa:
                frases_extraidas = extrair_frases(ementa)
                if frases_extraidas:
                    resultados[row_id] = frases_extraidas
                    count += 1

        print(f"Processadas {total_linhas} linhas. Encontradas ementas com frases válidas em {count} registros.")

except Exception as e:
    print(f"Ocorreu um erro: {e}", file=sys.stderr)
    sys.exit(1)

json_output_path = "palavras_extraidas.json"
with open(json_output_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(resultados, jsonfile, ensure_ascii=False, indent=2)

print(f"\nResultados finais salvos em '{json_output_path}'. Baixando o arquivo...")
files.download(json_output_path)