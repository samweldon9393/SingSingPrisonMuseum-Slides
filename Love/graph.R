library(ggplot2)
library(tidyr)
library(patchwork)

# Data
df <- data.frame(
  Visit.Frequency = c("Non-visited", "Early visited", "Late visited", "Consistently visited"),
  No.Misconduct = c(66.8, 70.7, 78.0, 77.3),
  Low.Misconduct = c(27.6, 21.2, 21.2, 22.7),
  High.Misconduct = c(5.6, 8.1, 0.7, 0.0)
)

# Reshape to long format
misconduct_long <- pivot_longer(
  df,
  cols = c(No.Misconduct, Low.Misconduct, High.Misconduct),
  names_to = "Misconduct.Level",
  values_to = "Percentage"
)

# Order the visitation levels
misconduct_long$Visit.Frequency <- factor(
  misconduct_long$Visit.Frequency,
  levels = c("Non-visited", "Early visited", "Late visited", "Consistently visited")
)

# Optional: clean label text
misconduct_long$Label <- paste0(round(misconduct_long$Percentage, 1), "%")

# Top plot (zoomed in)
p1 <- ggplot(misconduct_long, aes(x = Visit.Frequency, y = Percentage, color = Misconduct.Level, group = Misconduct.Level)) +
  geom_line(size = 1.2) +
  geom_point(size = 3) +
  geom_text(aes(label = Label), vjust = -0.8, size = 3) +
  scale_y_continuous(limits = c(60, 80)) +
  labs(x = "", y = "Percentage") +
  theme_minimal() +
  theme(legend.position = "none")  # Remove legend here

# Bottom plot (zoomed in)
p2 <- ggplot(misconduct_long, aes(x = Visit.Frequency, y = Percentage, color = Misconduct.Level, group = Misconduct.Level)) +
  geom_line(size = 1.2) +
  geom_point(size = 3) +
  geom_text(aes(label = Label), vjust = -0.8, size = 3) +
  scale_y_continuous(limits = c(0, 30)) +
  labs(x = "Visitation Pattern", y = "Percentage") +
  theme_minimal()

# Combine with single centered title
combined_plot <- (p1 / p2) +
  plot_annotation(
    title = "Misconduct Levels by Visitation Group",
    theme = theme(plot.title = element_text(hjust = 0.5, size = 16))
  )

# Show and save
combined_plot
ggsave("misconduct_broken_axis.png", plot = combined_plot, width = 8, height = 8)

