"""ANN para regressão usando scikit-learn."""
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=1200, n_features=12, noise=12, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

model = make_pipeline(
    StandardScaler(),
    MLPRegressor(hidden_layer_sizes=(64, 32), activation="relu",
                 max_iter=800, random_state=42)
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("RMSE:", mean_squared_error(y_test, pred) ** 0.5)
