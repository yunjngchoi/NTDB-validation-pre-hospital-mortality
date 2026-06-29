# NTDB Validation: Prehospital ED Mortality Prediction

This repository contains analysis code for the NTDB-based external validation of a prehospital emergency department mortality prediction model for trauma patients.

## Overview

This project evaluates the generalizability of a previously developed prehospital real-time AI model for predicting emergency department mortality in trauma patients.

The model was developed using prehospital variables available before or at emergency department arrival and validated across multi-institutional and multi-national trauma cohorts.

The main goal is to assess whether the model maintains robust predictive performance, calibration, clinical utility, and interpretability when applied to the large-scale U.S. NTDB cohort.

## Model

The model is an ensemble-based prediction model using:

- XGBoost
- LightGBM
- Random Forest

The input variables include 21 prehospital variables, which are expanded into 149 features after one-hot encoding.

The outcome is emergency department mortality.

## Datasets

The analysis includes:

- KTDB train/test cohort
- Korean external validation cohorts: CNUH, CHGH, CBUH, and GUGC
- Australian external validation cohort: WH
- U.S. external validation cohort: NTDB

Raw patient-level data are not included due to privacy restrictions and data use agreements.

## NTDB Validation Strategy

The NTDB cohort is split into tuning and validation datasets using a stratified 1:1 split.

The tuning dataset is used only for threshold optimization based on Youden's J statistic. The validation dataset is evaluated independently.

Both the original KTDB-derived threshold and the NTDB-optimized threshold are evaluated.

The purpose is to assess whether the classification threshold derived from the Korean cohort can be directly transported to the U.S. NTDB cohort, and whether local threshold tuning improves classification performance without model retraining.

## Missing Data Strategy

Several prehospital variables are unavailable across all NTDB years or partially unavailable in specific years.

The analysis compares multiple missing data handling approaches:

- Train-dataset mean imputation
- Missing-category mapping
- All-zero encoding

Train-dataset mean imputation is used as the primary strategy because it reduced out-of-distribution encoding patterns and avoided excessive reliance on dataset-specific missingness signals.

## Analyses

### Analyses Consistent with the Previous Paper

These analyses are performed to ensure methodological consistency with the original study and to evaluate whether the previously developed prehospital AI model remains valid in the NTDB cohort.

#### Shock Index Comparison

The proposed model is compared with Shock Index, a conventional physiologic triage indicator based on heart rate and systolic blood pressure.

The purpose is to determine whether the prehospital AI model provides better ED mortality prediction than a simple and widely used physiologic risk marker.

#### Calibration Curve

Calibration analysis is performed to compare predicted ED mortality risk with observed ED mortality.

The purpose is to assess whether the model provides reliable probability estimates, not only discrimination between survivors and non-survivors.

#### Decision Curve Analysis

Decision curve analysis is used to evaluate the clinical net benefit of the model across different mortality risk thresholds.

The purpose is to assess whether the model could provide practical clinical value compared with default strategies such as treating all patients or treating no patients as high risk.

#### SHAP-Based Model Interpretation

SHAP analysis is used to examine the contribution of individual prehospital predictors to model predictions.

The purpose is to assess whether the model's decision-making patterns are clinically interpretable and whether the most important predictors remain consistent across validation cohorts.

### Analyses Beyond the Previous Paper

These analyses extend the previous work by evaluating temporal robustness, subgroup performance, and predictor distribution shifts between KTDB and NTDB.

#### Temporal Performance Analysis

Year-by-year validation is performed in the NTDB cohort.

The purpose is to examine whether model performance remains stable over time or varies across calendar years, potentially reflecting changes in trauma systems, registry coding, variable availability, or clinical practice.

#### Subgroup Performance Analysis

Model performance is evaluated across clinically relevant patient subgroups, including:

- Age
- Sex
- Mechanism of injury
- Anatomical severity
- Physiologic severity
- Prehospital cardiac arrest availability

The purpose is to assess model robustness across different patient groups and identify potential performance heterogeneity.

#### Predictor Trend Interpretation

Predictor distribution and feature importance patterns are compared between KTDB and NTDB.

The purpose is to evaluate whether differences in variable availability, predictor distributions, and clinical characteristics may explain performance differences between the Korean and U.S. cohorts.

This analysis also helps identify potential covariate shift and assess the transportability of the model across countries.

#### PHCA Availability Analysis

Separate analyses are conducted for NTDB years with and without prehospital cardiac arrest information.

The purpose is to quantify the impact of prehospital cardiac arrest availability on model performance and to assess how missing key predictors affect external validation.

## Data Availability

Raw patient-level trauma registry data are not included in this repository.

This repository does not contain protected health information, identifiable patient data, or institution-specific identifiers.

## License

For academic and research use only.
