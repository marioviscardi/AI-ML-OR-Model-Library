from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
X,y=load_breast_cancer(return_X_y=True); m=VotingClassifier([('lr',LogisticRegression(max_iter=1000)),('svm',SVC(probability=True)),('rf',RandomForestClassifier(n_estimators=100,random_state=42))],voting='soft').fit(X,y); print(m.score(X,y))
