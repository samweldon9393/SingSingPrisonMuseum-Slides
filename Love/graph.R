library(ggplot2)
library(tidyr)

df <- data.frame(
    Visit.Frequency = c("Non-visited", "Early visited", "Late visited", "Consistently visited"),
    No.Misconduct = c(66.8, 70.7, 78.0, 77.3),
    Low.Misconduct = c(27.6, 21.2, 21.2, 22.7),
    High.Misconduct = c(5.6, 8.1, 0.7, 0.0)
)

# Reshape
misconduct_long <- pivot_longer(    
    df,
    cols = c(No.Misconduct, Low.Misconduct, High.Misconduct),
    names_to = "Misconduct.Level",
    values_to = "Percentage"
)

# Set order of visitation groups
misconduct_long$Visit.Frequency <- factor(
    misconduct_long$Visit.Frequency,
    levels = c("Non-visited", "Early visited", "Late visited", "Consistently visited")
)

ggplot(misconduct_long, aes(x = Visit.Frequency, y = Percentage, color = Misconduct.Level, group = Misconduct.Level)) +
  geom_line(size = 1.2) +
  geom_point(size = 3) +
  labs(title = "Misconduct Levels by Visitation Pattern",
       x = "Visitation Pattern",
       y = "Percentage",
       color = "Misconduct Level") +
  scale_color_manual(values = c(
    "No.Misconduct" = "#1b7837",
    "Low.Misconduct" = "#f6e8c3",
    "High.Misconduct" = "#762a83"
  )) +
  theme_minimal()

