# When Two Wrongs Don't Make a Right: Confirmation Bias under Time Pressure in AI-Assisted Medical Decision-Making]{"When Two Wrongs Don't Make a Right" - Examining Confirmation Bias and the Role of Time Pressure During Human-AI Collaboration in Computational Pathology

## Overview

This repository provides the software source code and materials used in *When Two Wrongs Don't Make a Right: Confirmation Bias under Time Pressure in AI-Assisted Medical Decision-Making]{"When Two Wrongs Don't Make a Right" - Examining Confirmation Bias and the Role of Time Pressure During Human-AI Collaboration in Computational Pathology*. We quantified confirmation bias triggered by AI-induced false confirmation and examined the role of time constraints in a web-based experiment, where trained pathology experts (n=28) estimated tumor cell percentages.
For a visual overview of our study setup, please refer to the teaser image below:
<img src="paperFigures/teaser.png" width="800px" align="center"/>


## Contents

- **ExperimentApplication:** The `ExperimentApplication/` directory contains the Django project source code for the experiment interface where participants rated tumor cell percentages. The `static/` subdirectory houses the study materials, including image patches from different H&E stained tissue slides (licensed under Creative Commons) and a table with additional information on these study images.
- **DataAnalysis** The `DataAnalysis/` directory contains the R source code (`ConfirmationBias-LMMs/` subdirectory) utilized to analyze the presence of confirmation bias during medical decision-making via linear mixed-effects models. An Excel file with the anonymized experiment data is also provided. Additionally, Jupyter notebooks, emplyed to assess the normality of the aforementioned study data and and generate the descriptive statistics and plots presented in the paper, are also included.
- containing code to asses the normal distribution of the experiment data, generate the descritpive statistcs and plots reported in the paper.

## License

The images located in the ```ExperimentApplication/static``` directory were obtained with the necessary rights and modified (e.g., visualization of cell detections) to meet our specific requirements. As a result, we are able to publish these images for public use under the Creative Commons 4.0 BY-NC-SA License.
