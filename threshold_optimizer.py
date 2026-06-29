def threshold_optimizer(
    proba,
    label,
    thresholds=None,
    verbose=True
):

    proba = np.asarray(proba).ravel()
    label = np.asarray(label).ravel()

    if thresholds is None:
        thresholds = np.arange(0, 1.01, 0.01)

    tuning_results = []

    best_threshold = 0.5
    best_youden = -np.inf

    for threshold in thresholds:
        pred = (proba >= threshold).astype(int)

        tn, fp, fn, tp = confusion_matrix(label, pred).ravel()

        specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
        sensitivity = tp / (tp + fn) if (tp + fn) != 0 else 0
        precision = tp / (tp + fp) if (tp + fp) != 0 else 0
        balanced_accuracy = (sensitivity + specificity) / 2

        youden_j = sensitivity + specificity - 1

        tuning_results.append({
            "Threshold": threshold,
            "Sensitivity": sensitivity,
            "Specificity": specificity,
            "Precision": precision,
            "Balanced Accuracy": balanced_accuracy,
            "Youden J": youden_j,
            "TN": tn,
            "FP": fp,
            "FN": fn,
            "TP": tp
        })

        if youden_j > best_youden:
            best_youden = youden_j
            best_threshold = threshold

    tuning_df = pd.DataFrame(tuning_results)

    if verbose:
        print(f"Best Threshold: {best_threshold:.3f}")
        print(f"Youden's J: {best_youden:.3f}")

    return best_threshold, tuning_df