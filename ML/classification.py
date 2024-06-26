import pickle
import pandas as pd
from preprocessing import text_preprocessing


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier


# загрузка датасета из файла
data = {'Реплика':[], 'Категория':[]}
for line in open('dataset.txt'):
    doc_line = line.split('@')
    data['Реплика'].append(doc_line[0])
    data['Категория'].append(doc_line[1].strip())
df = pd.DataFrame(data)


x = df.Реплика
y = df.Категория


#обучение
text_clf = Pipeline([

('tfidf', TfidfVectorizer(ngram_range=(1,2))), 
('clf', KNeighborsClassifier(n_neighbors=100))])

text_clf = text_clf.fit(x, y)
with open ('data.pickle', 'wb') as f:
    pickle.dump(text_clf, f )
