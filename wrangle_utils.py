import re
import emoji
from nltk.corpus import stopwords
from qalsadi import lemmatizer
import nltk

# Ensure NLTK stopwords downloaded
nltk.download('stopwords')

lemmer = lemmatizer.Lemmatizer()

# Define stopwords (your custom list can go here)
custom_stopwords = set([
    'و', 'أو', 'يعني', 'طب', 'كده', 'أوي', 'بقى', 'بس', 'حتى', 'خلاص', 'أصلا', 'مثلا',
    'لسه', 'لغاية', 'كمان', 'برضه', 'أهو', 'زي', 'تقريبًا', 'راح', 'جاب', 'قال', 'كان',
    'جت', 'جات', 'أنا', 'إنت', 'إنتي', 'هو', 'هي', 'إحنا', 'أنتو', 'هما', 'إيه', 'ليه', 'إمتى',
    'فين', 'ازاي', 'بعد', 'عاد', 'تو', 'لا هنت', 'لحين', 'للحين', 'هاك', 'صار', 'جان', 'خله',
    'سوه', 'شنو', 'ليش', 'متى', 'وين', 'شلون', 'ترى', 'وراك', 'زي كذا', 'أبد', 'واجد', 'صدق',
    'أكيد', 'ألحين', 'الحين', 'عطاه', 'وش', 'كيف',
])
nltk_stopwords = set(stopwords.words('arabic'))
negation_words = {"مش", "ما", "لا", "ليس", "لن", "لم", "بدون", "غير", "إلا", "لكن"}
all_stopwords = (nltk_stopwords | custom_stopwords) - negation_words

def remove_diacritics(text):
    return re.sub(r'[\u064B-\u065F\u0670]', '', text)

def normalize_arabic(text):
    text = remove_diacritics(text)
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    text = text.replace("ى", "ي").replace("ة", "ه")
    return text

def remove_elongation(text):
    def correct(match):
        char = match.group(1)
        return char * 2  # Ensure elongation is reduced to exactly 2 occurrences
    return re.sub(r'(.)\1{2,}', correct, text)  # Pass text as the last argument


def remove_stopwords(text):
    words = text.split()
    return ' '.join([w for w in words if w in negation_words or w not in all_stopwords])

# Use the lemmatizer inside a context manager
def clean_text(text):
    text = str(text).strip()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = remove_diacritics(text)
    text = normalize_arabic(text)
    text = remove_elongation(text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Initialize the lemmatizer directly (outside of a context manager)
    lemmer = lemmatizer.Lemmatizer()
    text = " ".join(lemmer.lemmatize_text(text))  # Lemmatization step
    
    text = remove_stopwords(text)
    return text
