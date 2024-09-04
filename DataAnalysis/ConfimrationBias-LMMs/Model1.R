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
# distance from AI-assisted estimation to GT has to exceed 5% (incorrect assessment Q2 & Q3) to indicate a notable bias
df <- df[df$EstAI2GT > 5 | df$EstAI2GT < -5, ]
# distances from EstB2GT, PredAI2GT, EstAI2GT all must have the same sign to suggest a consistent tendency for over-/ underestimation between human and machine
df <- df[(df$PredAI2GT * df$EstB2GT) >= 0, ]
df <- df[((df$EstB2GT * df$EstAI2GT) >= 0) & ((df$PredAI2GT * df$EstAI2GT) >= 0), ]
# presence of time pressure during TCP assessment (consistent across both EstB & EstAI) dummy coded as: 0 = without time pressure, 1 = with time pressure
# comment this in for Model 1.1
# df <- df[df$TP == 0, ]
# comment this in for Model 1.2
# df <- df[df$TP == 1, ]


# Fit the Linear Mixed-Effects Model
model <- lmer(EstAI2PredAI ~ PredAI2EstB + (1 | participant_id), data = df)
summary(model)
#confint(model, level = 0.95)
packageVersion("lme4")
R.version