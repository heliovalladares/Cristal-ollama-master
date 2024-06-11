import random
import pandas as pd

# Base phrases and their categories
base_phrases = [
    ("Recomende um jogo de ação emocionante", 1),
    ("Quais são os melhores simuladores de agricultura?", 2),
    ("Eu gosto de jogos de estratégia complexos, o que você recomenda?", 3),
    ("Procuro um RPG com uma história envolvente", 4),
    ("Quais são os jogos mais populares atualmente?", 5),
    ("Recomende um bom jogo de aventura para crianças.", 6),
    ("Quais jogos têm os melhores gráficos?", 7),
    ("Quais são os lançamentos mais recentes no gênero RPG?", 8),
    ("Se gostei de [Jogo X], o que mais eu devo jogar?", 9),
    ("Quais jogos são semelhantes a [Jogo Y]?", 10)
]

# Synonyms and variations
synonyms = {
    "Recomende": ["Sugira", "Indique", "Me mostre"],
    "jogo de ação emocionante": ["jogo de ação eletrizante", "jogo de ação empolgante", "jogo de ação intenso"],
    "melhores": ["top", "principais", "mais recomendados"],
    "simuladores de agricultura": ["jogos de simulação agrícola", "simuladores de fazenda", "simuladores agrícolas"],
    "Eu gosto de": ["Prefiro", "Sou fã de", "Eu curto"],
    "complexos": ["desafiadores", "difíceis", "intrincados"],
    "o que você recomenda?": ["alguma recomendação?", "o que você sugere?", "qual sua sugestão?"],
    "Procuro": ["Estou procurando por", "Busco", "Gostaria de encontrar"],
    "uma história envolvente": ["uma trama cativante", "um enredo interessante", "uma narrativa envolvente"],
    "populares": ["famosos", "conhecidos", "bem avaliados"],
    "atualmente": ["no momento", "hoje em dia", "agora"],
    "bom": ["ótimo", "excelente", "ideal"],
    "para crianças": ["infantil", "para os pequenos", "adequado para crianças"],
    "melhores gráficos": ["gráficos mais bonitos", "visual mais impressionante", "melhor qualidade gráfica"],
    "lançamentos mais recentes": ["novidades mais recentes", "jogos lançados recentemente", "últimos lançamentos"],
    "Se gostei de": ["Se eu curti", "Se eu adorei", "Se eu gostei de"],
    "o que mais eu devo jogar?": ["que outros jogos devo tentar?", "qual outro jogo você recomenda?", "quais outros jogos devo experimentar?"],
    "semelhantes a": ["parecidos com", "similares a", "com características semelhantes a"]
}

# Function to generate variations
def generate_variations(base_phrases, synonyms, n):
    queries = []
    while len(queries) < n:
        for phrase, label in base_phrases:
            words = phrase.split()
            new_phrase = []
            for word in words:
                if word in synonyms:
                    new_phrase.append(random.choice(synonyms[word]))
                else:
                    new_phrase.append(word)
            new_phrase = " ".join(new_phrase)
            queries.append((new_phrase, label))
            if len(queries) >= n:
                break
    return queries

# Generate 1000 queries
queries = generate_variations(base_phrases, synonyms, 1000)

# Shuffle the queries to ensure randomness
random.shuffle(queries)

# Create DataFrame
df = pd.DataFrame(queries, columns=["text", "label"])

# Save to CSV
file_path = "game_recommendation_queries_unique.csv"
df.to_csv(file_path, index=False)

# Display the first few rows
df.head(), file_path
