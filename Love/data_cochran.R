library(ggplot2)

visitation_groups <- data.frame(
    "Visit Frequency" = c("No Visits", "Visited Early", "Visited Late", "Consistently Visited"),
    "Group Size" = c(75, 11, 9, 6)
)

#visitation_groups <- c(
#    "No Visits" = 75,
#    "Visited Early" = 11,
#    "Visited Late" = 9,
#    "Consistently Visited" = 6
#)
misconduct_groups <- c(
    "No Misconduct" = 69,
    "Some Misconduct" = 26,
    "Heavy Misconduct" = 5
)

# Make pie chart
p <- ggplot(visitation_groups, aes(x = "", y = Group.Size, fill = Visit.Frequency)) +
  geom_bar(stat = "identity", width = 1) +        # Create bar chart with one bar
  coord_polar("y", start = 0) +                   # Turn bar chart into pie chart
  labs(title = "Inmate Visitation Groupings") +
  theme_void() +                                  # Remove axes and background
  theme(legend.title = element_blank())           # Remove legend title

ggsave("visitation_pie_chart.png", plot = p, width = 6, height = 6)
