library(ggplot2)

df <- data.frame(
    Visit.Frequency = c("Non-visited", "Early visited", "Late visited", "Consistently visited"),
    No.Misconduct = c(66.8, 70.7, 78.0, 77.3),
    Low.Misconduct = c(27.6, 21.2, 21.2, 22.7),
    High.Misconduct = c(5.6, 8.1, 0.7, 0.0)
)

df
