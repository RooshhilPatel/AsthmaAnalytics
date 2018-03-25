#DEMOGRAPHIC PLOTS

# GENDER
library(ggplot2)

# Veritcal ggplot
ggplot(sexByState2, aes(y = State, x = Percent, label = Percent, fill = Sex, colour = Sex)) +
  geom_segment(aes(x = 0, y = State, xend = Percent, yend = State), color = "grey50", size = 0.75) +
  geom_point(size = 3) +
  labs(title="Asthma Percentages Per State Per Sex", 
       subtitle="Male vs. Female") + 
  coord_flip()

# to add percentages on dots
# geom_text(nudge_x = 1.5, angle = 0) + 





# AGE
library(ggplot2)

#grouped
ggplot(ageByState, aes(y = Percent, x = State, label = Percent, fill = Age, colour = Age)) + 
  geom_bar(stat="identity", width=.5, position="dodge") + 
  labs(title="Asthma Percentages Per State Per Age Group", 
       subtitle="Ages 18-24, 25-34, 35-44, 45-54, 55-64, 65+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + coord_flip()

#stacked
ggplot(ageByState, aes(y = Percent, x = State, label = Percent, fill = Age, colour = Age)) + 
  geom_bar(stat="identity", width=.5) + 
  labs(title="Asthma Percentages Per State Per Age Group", 
       subtitle="Ages 18-24, 25-34, 35-44, 45-54, 55-64, 65+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + coord_flip()



# INCOME
library(ggplot2)

#grouped
ggplot(incomeByState, aes(y = Percent, x = State, label = Percent, fill = Income, colour = Income)) + 
  geom_bar(stat="identity", width=.5, position="dodge") + 
  labs(title="Asthma Percentages Per State Per Income Group", 
       subtitle="Incomes <$15k, $15k-$24,999, $25k-$49,999, $50k-$74,999, $75k+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

#stacked
ggplot(incomeByState, aes(y = Percent, x = State, label = Percent, fill = Income, colour = Income)) + 
  geom_bar(stat="identity", width=.5) + 
  labs(title="Asthma Percentages Per State Per Income Group", 
       subtitle="Incomes <$15k, $15k-$24,999, $25k-$49,999, $50k-$74,999, $75k+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


# INCOME SPLIT 1 
#grouped
ggplot(incomeByState2, aes(y = Percent, x = State, label = Percent, fill = Income, colour = Income)) + 
  geom_bar(stat="identity", width=.5, position="dodge") + 
  labs(title="Asthma Percentages Per State Per Income Group", 
       subtitle="Incomes <$15k, $15k-$24,999, $25k-$49,999, $50k-$74,999, $75k+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

# INCOME SPLIT 2
#grouped
ggplot(incomeByState2_2, aes(y = Percent, x = State, label = Percent, fill = Income, colour = Income)) + 
  geom_bar(stat="identity", width=.5, position="dodge") + 
  labs(title="Asthma Percentages Per State Per Income Group", 
       subtitle="Incomes <$15k, $15k-$24,999, $25k-$49,999, $50k-$74,999, $75k+") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))





# RACE
library(ggplot2)

#grouped
ggplot(raceByState, aes(y = Percent, x = State, label = Percent, fill = Race, colour = Race)) + 
  geom_bar(stat="identity", width=.5, position="dodge") + 
  labs(title="Asthma Percentages Per State Per Race Group", 
       subtitle="Races White, Black, Multi, Other") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

#stacked
ggplot(raceByState, aes(y = Percent, x = State, label = Percent, fill = Race, colour = Race)) + 
  geom_bar(stat="identity", width=.5) + 
  labs(title="Asthma Percentages Per State Per Race Group", 
       subtitle="Races White, Black, Multi, Other") + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6))
