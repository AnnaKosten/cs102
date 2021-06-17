setwd("C:/Users/User/cs102/homework07/r")
adult <- read.csv("adult_data.csv", header=T)

head(adult)

sapply(adult, function(x) sum(is.na(x)))

# 1. —колько мужчин и женщин (признак sex) представлено в этом наборе данных?
table(adult$sex)

# 2.  аков средний возраст (признак age) женщин?
mean(subset(adult, sex == "Female")$age)

# 3.  акова дол€ граждан √ермании (признак native-country)?
sum(adult$native.country == "Germany") / nrow(adult)

# 4-5.  аковы средние значени€ и среднеквадратичные отклонени€ возраста тех, 
# кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год?

rich <- subset(adult, salary == ">50K")
poor <- subset(adult, salary == "<=50K")
mean(rich$age)
sd(rich$age)
mean(poor$age)
sd(poor$age)

# 6. ѕравда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? 
# (признак education Ц Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)

table(rich$education)

# 7. ¬ыведите статистику возраста дл€ каждой расы (признак race) и каждого пола.
# Ќайдите таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.

for(i in unique(adult$race)) {
  print(i)
  for(j in unique(adult$sex)) {
    print(j)
    print(summary(subset(adult, race == i & sex == j)$age))
  }
}

max(subset(adult, race == "Amer-Indian-Eskimo" & sex == "Male")$age)
# 8. ѕравда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? 
# (признак education Ц Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)

mmen <- subset(adult, sex == "Male" & (substr(marital.status, 1, 7) == "Married"))
sum(mmen$salary == ">50K") / nrow(mmen)
bmen <- subset(adult, sex == "Male" & (substr(marital.status, 1, 7) != "Married"))
sum(bmen$salary == ">50K") / nrow(bmen)

# 9. акое максимальное число часов человек работает в неделю (признак hours-per-week)?
# —колько людей работают такое количество часов и каков среди них процент зарабатывающих много?

max(adult$hours.per.week)
workers <- subset(adult, hours.per.week == max(adult$hours.per.week))
nrow(workers)
sum(workers$salary == ">50K") / nrow(workers) * 100

# 10. ѕосчитайте среднее врем€ работы (hours-per-week) зарабатывающих мало и много 
# (salary) дл€ каждой страны (native-country).

for(i in unique(adult$native.country)) {
  print(i)
  print(mean(subset(poor, native.country == i)$hours.per.week))
  print(mean(subset(rich, native.country == i)$hours.per.week))
}
