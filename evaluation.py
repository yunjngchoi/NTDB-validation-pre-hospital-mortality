def evaluation_threshold(proba, label, threshold, verbose=True):

    proba = np.asarray(proba).ravel()
    label = np.asarray(label).ravel()

    pred = (proba >= threshold).astype(int)

    tn, fp, fn, tp = confusion_matrix(label, pred).ravel()

    acc = (tp + tn) / (tp + tn + fp + fn)
    spe = tn / (tn + fp) if (tn + fp) != 0 else 0
    sen = tp / (tp + fn) if (tp + fn) != 0 else 0
    pre = tp / (tp + fp) if (tp + fp) != 0 else 0
    balacc = (spe + sen) / 2

    roc = roc_auc_score(label, proba)
    prc = average_precision_score(label, proba)

    base_rate = np.mean(label)

    adj_pre = (pre - base_rate) / (1 - base_rate) if base_rate < 1 else np.nan
    lift = pre / base_rate if base_rate > 0 else np.nan
    apg = (prc - base_rate) / (1 - base_rate) if base_rate < 1 else np.nan
    nprc = prc / base_rate if base_rate > 0 else np.nan

    results = {
        "Threshold": threshold,
        "Accuracy": acc,
        "Specificity": spe,
        "Sensitivity": sen,
        "Precision": pre,
        "Adjusted Precision": adj_pre,
        "Lift": lift,
        "Balanced Accuracy": balacc,
        "AUROC": roc,
        "AUPRC": prc,
        "APG": apg,
        "nAUPRC": nprc,
        "Base Rate": base_rate,
        "TN": tn,
        "FP": fp,
        "FN": fn,
        "TP": tp
    }

    if verbose:
        print(
            f"Threshold: {threshold:.3f}\n"
            f"Accuracy: {acc:.3f}, "
            f"Specificity: {spe:.3f}, "
            f"Sensitivity: {sen:.3f}, "
            f"Precision: {pre:.3f}, "
            f"Adjusted Precision: {adj_pre:.3f}, "
            f"Lift: {lift:.3f}, "
            f"Balanced Accuracy: {balacc:.3f}, "
            f"AUROC: {roc:.3f}, "
            f"AUPRC: {prc:.3f}, "
            f"APG: {apg:.3f}, "
            f"nAUPRC: {nprc:.3f}\n"
        )

    return results
