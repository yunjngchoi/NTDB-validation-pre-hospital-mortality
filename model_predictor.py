def model_predictor(
    data,
    xgb_model,
    lgbm_model,
    rf_model,
    beta_calibrator,
    feature_columns,
    label_col="survive",
    apply_calibration=True
):

    X_eval = data[feature_columns].copy()
    y_eval = data[label_col].astype(int).values

    xgb_proba = xgb_model.predict_proba(X_eval)[:, 1]
    lgbm_proba = lgbm_model.predict_proba(X_eval)[:, 1]
    rf_proba = rf_model.predict_proba(X_eval)[:, 1]

    ensemble_proba = np.mean(
        [xgb_proba, lgbm_proba, rf_proba],
        axis=0
    )

    if apply_calibration:
        final_proba = beta_calibrator.predict(ensemble_proba)
    else:
        final_proba = ensemble_proba

    return (
        X_eval,
        y_eval,
        xgb_proba,
        lgbm_proba,
        rf_proba,
        ensemble_proba,
        final_proba
    )