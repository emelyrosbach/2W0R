if (!require(readxl)) install.packages("readxl")
if (!require(lme4)) install.packages("lme4")
if (!require(lme4)) install.packages("lmerTest")

# load the necessary libraries
library(readxl)
library(lme4)
library(lmerTest)

# read the data from the Excel file
# current R working directory
getwd()
# set path to where this R file & the data ecxel are located
setwd("../Desktop/CHI25/DataAnalysis")
df <- read_excel('./data.xlsx')

# filter samples: split into tertiles based on correctness of AI-aided assessment
# Result: Q1=correct 0-5%, Q2=minor error 6-12%, Q3=severe error 13-79% -> Q2 & Q3 = incorrect
# distances from the baseline and AI-assisted estimate to the GT exceed 5% (incorrect assessment Q2 & Q3), indicating a notable bias/ error
df <- df[df$ABS_EstB2GT > 5 & df$ABS_EstAI2GT > 5, ]


# Model2
# for the AI prediction to be considered congruent, its distance from the GT also has to exceed 5%
df <- df[df$ABS_PredAI2GT > 5, ]
# distances from EstB2GT, PredAI2GT, EstAI2GT all must have the same sign to suggest a consistent tendency for over-/ underestimation between human and machine
df <- df[(df$PredAI2GT * df$EstB2GT) > 0, ]
df <- df[((df$EstB2GT * df$EstAI2GT) > 0) & ((df$PredAI2GT * df$EstAI2GT) > 0), ]
# for the AI prediction to be considered congruent, it also has to be close to the baseline estimate
# here the dataset is split based on the median distance from the AI predictions to the baseline estimatesdf <- df[abs(df$AI2B) <= 15, ]
df <- df[abs(df$PredAI2EstB) <= 15, ]

# Model3 (Comment out Model 2, before commenting this in)
# for the AI prediction to be considered incongruent, it has to be further away from the baseline estimate
# df <- df[abs(df$PredAI2EstB) > 15, ]

# Fit the Linear Mixed-Effects Model
model <- lmer(EstAI ~ EstB + PredAI + (1 | participant_id), data = df)
summary(model)