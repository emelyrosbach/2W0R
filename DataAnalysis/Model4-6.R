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

# comment this in for Model4 - correct
df <- df[(abs(df$EstAI2GT) >= 0) & (abs(df$EstAI2GT) <= 5), ]

# comment this in for Model5 - minor error
# df <- df[(abs(df$EstAI2GT) > 5) & (abs(df$EstAI2GT) <= 12), ]

# comment this in for Model6 - severe error
# df <- df[(abs(df$EstAI2GT) > 12) & (abs(df$EstAI2GT) <= 79), ]

# Fit the Linear Mixed-Effects Model
model <- lmer(EstAI2PredAI ~ PredAI2EstB + (1 | participant_id), data = df)
summary(model)