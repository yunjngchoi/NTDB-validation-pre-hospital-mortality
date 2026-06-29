def model_loader(model_path):

    model_dict = joblib.load(model_path)

    xgb_model = model_dict["xgb_model"]
    lgbm_model = model_dict["lgbm_model"]
    rf_model = model_dict["rf_model"]
    beta_calibrator = model_dict["beta_calibrator"]
    feature_columns = model_dict["feature_columns"]

    return model_dict, xgb_model, lgbm_model, rf_model, beta_calibrator, feature_columns