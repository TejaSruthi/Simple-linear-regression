# load the datset
datset = read.csv('Salary_Data.csv')

library('caTools')
set.seed(123)
split = sample.split(datset$Salary, SplitRatio = 2/3)
train_set = subset(datset, split == TRUE)
test_set = subset(datset, split == FALSE)

# fitting simple linear regression to train_set 
regressor = lm(formula = Salary ~ YearsExperience, data = train_set)

# prdict test_set results
y_pred = predict(regressor, newdata = test_set)

# visualising the train_set
# install.packages('ggplot2')
library('ggplot2')
ggplot() +
  geom_point(aes(x = train_set$YearsExperience, y = train_set$Salary),
             colour = 'red') +
  geom_line(aes(x = train_set$YearsExperience, y = predict(regressor, newdata = train_set)),
             colour = 'blue') +
  ggtitle('Salary vs Experience (Training set)') + 
  xlab('Years of Experience') +
  ylab('Salary') 

# visualising the train_set
# library('ggplot2')
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'black') + 
  geom_line(aes(x = train_set$YearsExperience, y = predict(regressor, newdata = train_set)),
            colour = 'blue') + 
  ggtitle('Salary vs Experience (Test set)') + 
  xlab('Years of experience') + 
  ylab('Salary')