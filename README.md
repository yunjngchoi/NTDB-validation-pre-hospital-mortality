# NTDB Validation: Prehospital ED Mortality Prediction

This repository contains analysis code for NTDB-based external validation and extended evaluation of a prehospital emergency department mortality prediction model for trauma patients.

## Study Aim

This study aims to evaluate whether a prehospital ED mortality prediction model developed using KTDB can be generalized to external trauma cohorts, particularly the U.S. NTDB cohort.

## Model Summary

The model is an ensemble-based prediction model.

- Algorithms: XGBoost, LightGBM, and Random Forest
- Input variables: 21 prehospital variables
- Feature format: 149 one-hot encoded features
- Output variable: emergency department mortality
- Calibration method: beta calibration

## Datasets

The analysis includes:

- KTDB train/test cohort
- Korean external validation cohorts
- Australian external validation cohort: WH
- U.S. external validation cohort: NTDB

Raw patient-level data are not included due to privacy restrictions and data use agreements.

## NTDB Validation Strategy

The NTDB cohort is split into tuning and validation datasets using a stratified 1:1 split.

The tuning dataset is used only for threshold optimization. The validation dataset is used for final model evaluation.

Both the KTDB-derived threshold and the NTDB-optimized threshold are evaluated to assess model transportability and the effect of local threshold tuning.

## Missing Data Strategy

Several prehospital variables are unavailable across all NTDB years or only available in selected years.

The following missing data handling methods are compared:

- Train-dataset mean imputation
- Missing-category mapping
- All-zero encoding

Train-dataset mean imputation is used as the primary strategy because it reduces out-of-distribution encoding patterns and avoids excessive reliance on dataset-specific missingness signals.

## Main Analyses

### Analyses Consistent with the Previous Paper

The following analyses are conducted to maintain methodological consistency with the previous study:

- Shock Index comparison
- Calibration curve
- Decision curve analysis
- SHAP-based model interpretation

The purpose of these analyses is to evaluate whether the model maintains performance, calibration, clinical utility, and interpretability in the NTDB cohort, while also comparing it with a conventional physiologic triage indicator.

### Analyses Beyond the Previous Paper

Additional analyses are conducted to evaluate temporal robustness, subgroup performance, and predictor differences between KTDB and NTDB.

These analyses include:

- Temporal performance analysis
- Subgroup performance analysis
- Predictor trend interpretation
- Prehospital cardiac arrest availability analysis

The purpose is to assess whether model performance remains stable over time, whether performance differs across clinically important subgroups, and whether differences in predictor distributions or feature importance patterns help explain transportability between KTDB and NTDB.

Candidate subgroup analyses include age, sex, mechanism of injury, anatomical severity, physiologic severity, and prehospital cardiac arrest availability.

## File Structure

```text
.
├── model                 # Final saved model file used for external validation
├── model_loader.py       # Functions for loading the saved model and related objects
├── model_predictor.py    # Functions for predicting and calibrating
├── threshold_optimizer.py  # Threshold selection and optimization utilities
├── evaluation.py         # Evaluation utilities, including threshold-based metrics
└── README.md             # Project overview and usage instructions
```


## License

For academic and research use only.
