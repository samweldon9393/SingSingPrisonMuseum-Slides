library(ggplot2)

visitation_groups <- data.frame(
    "Visit Frequency" = c("No Visits", "Visited Early", "Visited Late", "Consistently Visited"),
    "Group Size" = c(75, 11, 9, 6)
)

misconduct_groups <- data.frame(
    "Misconduct Frequency" = c("No Misconduct", "Some Misconduct", "Heavy Misconduct"),
    "Group Size" = c(69, 26, 5)
)

visit_colors <- c(
  "No Visits" = "#d73027",
  "Visited Early" = "#fc8d59",
  "Visited Late" = "#91bfdb",
  "Consistently Visited" = "#4575b4"
)

misconduct_colors <- c(
  "No Misconduct" = "#d73027",
  "Some Misconduct" = "#fc8d59",
  "Heavy Misconduct" = "#4575b4"
)


# Make visit pie chart
p <- ggplot(visitation_groups, aes(x = "", y = Group.Size, fill = Visit.Frequency)) +
  geom_bar(stat = "identity", width = 1) +        # Create bar chart with one bar
  coord_polar("y", start = 0) +                   # Turn bar chart into pie chart
  scale_fill_manual(values = visit_colors) +
  labs(title = "Visitation Frequency") +
  theme_void() +                                  # Remove axes and background
  theme(legend.title = element_blank())           # Remove legend title

ggsave("visitation_pie_chart.png", plot = p, width = 6, height = 6)

# Make pie chart
p <- ggplot(misconduct_groups, aes(x = "", y = Group.Size, fill = Misconduct.Frequency)) +
  geom_bar(stat = "identity", width = 1) +        # Create bar chart with one bar
  coord_polar("y", start = 0) +                   # Turn bar chart into pie chart
  scale_fill_manual(values = misconduct_colors) +
  labs(title = "Misconduct Frequency") +
  theme_void() +                                  # Remove axes and background
  theme(legend.title = element_blank())           # Remove legend title

ggsave("misconduct_pie_chart.png", plot = p, width = 6, height = 6)
