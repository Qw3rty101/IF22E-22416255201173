from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

#Pemisahan Data
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#Membangun Model
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, Y_train)

#Membuat Prediksi
y_pred = dt_classifier.predict(X_test)

#Evaluasi Model
accuracy = accuracy_score(Y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

#Visualisasi Decision Tree
plt.figure(figsize=(12,8))
plot_tree(dt_classifier, filled=True, feature_names=iris.feature_names)
plt.show()

#Evaluasi Classification Report
classification_rep = classification_report(y_pred, Y_test)
print("Classification Report:\n", classification_rep)

#Visualisasi Hasil Klasifikasi
plt.figure(figsize=(10, 6))
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred, cmap='viridis', edgecolors='k', s=80, label='Predicted Class')
plt.title('Decision Tree Classification on Iris Data')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()