from dataviz import DataViz
from models import Model
from datawrapper import DataWrapper
import matplotlib.pyplot as plt


def main():
    data = DataWrapper()
    data.import_train_set_from_txt("./sat.trn")
    data.import_test_set_from_txt("./sat.tst")
    data.scale("normalize")

    # testdataviz = DataViz(data)
    testmodel = Model(data)
    models = []

    # Random Forest models :
    # for n_estimators in range(10, 50, 10):
    # models.append((testmodel.build_rf_bagging(n_estimators=n_estimators)))
    # accuracies, best_model, best_accuracy = testmodel.cross_validate(models, cv=10)

    # Decision tree model :
    # for depth in range(10, 50, 10):
    # models.append(testmodel.build_decisiontree(max_depth=depth))
    # accuracies, best_model, best_accuracy = testmodel.cross_validate(models, cv=10)

    # Logistic regression model :
    for max_iter in range(100, 200, 20):
        models.append(testmodel.build_logisticregression(max_iter=max_iter))
    accuracies, best_model, best_accuracy = testmodel.cross_validate(models, cv=10)

    print("-----")
    for a in accuracies:
        print(a)
    print(
        f"Best model: {best_model} with {best_accuracy} of accuracy.\n(Note: you need to fit the model in order to use it.)"
    )


if __name__ == "__main__":
    main()
