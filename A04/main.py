import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
nltk.download('stopwords')

# Texto de ejemplo en español
text = "María está sentada en la playa, escuchando las olas del mar y el canto de las aves. Siente una profunda paz."

# Tokenización
tokens = word_tokenize(text, language='spanish')
print("Tokens:", tokens)

# Eliminación de stopwords
stop_words = set(stopwords.words('spanish'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nFiltered Tokens:", filtered_tokens)

# Etiquetado de Partes del Discurso (POS Tagging)
pos_tags = pos_tag(filtered_tokens)
print("\nPOS Tags:", pos_tags)

# Extracción de Entidades Nombradas
named_entities = ne_chunk(pos_tags)
print("\nNamed Entities:")
for entity in named_entities:
    if hasattr(entity, 'label'):
        print(entity.label(), ' '.join(c[0] for c in entity))

# Análisis de Sentimientos
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(text)
print("\nSentiment Analysis:", sentiment)

# Validación Semántica y pragmática
if sentiment['compound'] > 0.5:
    print("\nEl sentimiento de la oración es positivo, lo cual coincide con el contexto de paz y tranquilidad en la playa.")
else:
    print("\nEl sentimiento no es fuertemente positivo, lo que podría indicar una desalineación en el contexto de paz.")
