setwd("C:/Users/User/cs102/homework07/r")

df <- read.csv("howpop_train.csv", encoding="UTF-8")

head(df)

df <- df[,!grepl("_lognorm$", names(df))]

sapply(df, function(x) sum(is.na(x)))

df$published = as.POSIXct(df$published, format = "%Y-%m-%d %H:%M:%S", tz = "GMT")

summary(df)

df$year <- as.numeric(format(df$published, '%Y'))
df$month <- as.numeric(format(df$published, '%m'))
df$weekday <- as.numeric(format(df$published, '%u'))
df$day <- as.numeric(format(df$published, '%d'))
df$hour <- as.numeric(format(df$published, '%H'))

# 1. В каком месяце (и какого года) было больше всего публикаций?
# март 2016
# март 2015
# апрель 2015
# апрель 2016

m15 <- subset(df, df$month == 3 & df$year == 2015)
m16 <- subset(df, df$month == 3 & df$year == 2016)
a15 <- subset(df, df$month == 4 & df$year == 2015)
a16 <- subset(df, df$month == 4 & df$year == 2016)

m <- rbind(c(nrow(m15), nrow(a15)), c(nrow(m16), nrow(a16)))
colnames(m) <- c("March", "April")
rownames(m) <- c(2015, 2016)

barplot(m, main = 'публикации в марте и апреле 2015 и 2016', ylab = "Publications",
        ylim = c(1500, 2200), xpd = F,
        col = c("darkorchid", "purple4"),
        legend = T, beside = T)

# 2. Проанализируйте публикации в месяце из предыдущего вопроса

# Выберите один или несколько вариантов:

#  * Один или несколько дней сильно выделяются из общей картины (да)

barplot(table(m15$day), main = 'Daily publications (March 2015)',
        ylab = 'Publications', xlab = 'Day',
        col = "purple3",
        legend = F, beside = T)

#  * На хабре всегда больше статей, чем на гиктаймсе (нет)

barplot(table(m15$domain, m15$day), main = 'Daily publications by domain (March 2015)',
        ylab = 'Publications', xlab = 'Day',
        col = c("darkorchid", "pink"),
        legend = T, beside = T)

#  * По субботам на гиктаймс и на хабрахабр публикуют примерно одинаковое число статей (да)

table(subset(m15, m15$weekday == 6)$domain)

# 3. Когда лучше всего публиковать статью?

#  * Больше всего просмотров набирают статьи, опубликованные в 12 часов дня (нет)
#  * Больше всего просмотров набирают статьи, опубликованные в 6 часов утра (да)

library(dplyr)

by_hour <- df %>% group_by(hour)

vcomms <- by_hour %>% summarise(
  avviews = mean(views),
  avcomms = mean(comments)
)

barplot(vcomms$avviews ~ vcomms$hour, main = 'среднее число просмотров в чаc',
        ylab = 'Views', xlab = 'Hour',
        ylim = c(14000, 21000), xpd = F, col = "darkorchid",
        legend = F, beside = T)

#  * У опубликованных в 10 утра постов больше всего комментариев (нет)

barplot(vcomms$avcomms ~ vcomms$hour, main = 'среднее число комментариев в час',
        ylab = 'Comments', xlab = 'Hour',
        ylim = c(30, 55), xpd = F, col = "darkorchid",
        legend = F, beside = T)

#  * Максимальное число комментариев на гиктаймсе набрала статья, опубликованная в 9 часов вечера (нет)

geek <- by_hour %>% filter(domain == 'geektimes.ru')
geek$published[which(geek$comments == max(geek$comments))]

#  * На хабре дневные статьи комментируют чаще, чем вечерние (нет)

habr <- by_hour %>% filter(domain == 'habrahabr.ru')

hcomms <- by_hour %>% summarise(
  avcomms = mean(comments)
)

plot(hcomms$avcomms ~ hcomms$hour, type = 'l', main = 'среднее число комментариев на хабре в час',
     ylab = 'Comments', xlab = 'Hour', col = 2)


# 4. Кого из топ авторов чаще всего минусуют?

# @Mordatyj
# @Mithgol
# @alizar
# @ilya42

by_author <- df %>% group_by(author)

top_4 <- by_author %>% filter(author %in% c('@Mordatyj', '@Mithgol', '@alizar', '@ilya42'))

na.exclude(top_4) %>% summarise(
  avmin = mean(votes_minus)
)


# 5. Сравните субботы и понедельники

# Правда ли, что по субботам авторы пишут в основном днём, а по
# понедельникам — в основном вечером? (нет)

mon_sat <- by_hour %>% filter(weekday %in% c(1, 6))

barplot(table(mon_sat$weekday, mon_sat$hour), main = 'количество публикаций в час по понедельникам и субботам',
        ylab = 'Publications', xlab = 'Hour',
        col = c("darkorchid", "pink"),
        legend = c('Mon', 'Sat'), beside = T)
