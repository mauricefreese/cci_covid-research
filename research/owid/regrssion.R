library(ggplot2)
library(dplyr)
library(broom)
library(ggpubr)

# importing data
df <- read.csv("/Users/mauricefreese/Downloads/econfour/research/owid/cur_us_owid_covid_monthly.csv", header = TRUE)

# model
str(df)