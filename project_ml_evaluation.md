#### SER594: Machine Learning Evaluation
#### Soccer Team and Similar Player Selection (title)
#### Amarjeet Singh (author)
#### 21 November 2022 (date)

## Evaluation Metrics
### Metric 1
Mean Absolute Percentage Error

The main reason for choosing the Mean Absolute Percentage Error is that as percentage
error is calculated in terms of absolute error so this avoids the problem of cancelling
out the positive and negative values. Also, this method is being referred as scale
independent because it allows the comparison for forecast of different scale. Lower value 
of MAPE, better the model will forecast the values.

### Metric 2
Root Mean Squared Error

### Justification
Root Mean Square is the standard deviation of prediction errors from the regression
line.It also tells us how concentrated the data is around the line of best fit.It
shows how far prediction values fall from measured true values using Euclidean 
distance. Also, it is very helpful to have single number to judge the model's 
performance whether during training, cross-validation etc. This is one of the most 
commonly used measures for evaluating the quality of predictions. 


## Alternative Models
1. Grid Search CV
**Construction:** 
Grid Search CV is process of performing hyperparameter tuning to find the optimal
values for given model. Here , I applied GridSearch CV to the linear regression 
model(same as that of our main model). Also, I applied cross validation 5 times to each 
of  selected hyperparameter.
**Evaluation:** 
In our given dataset as value of Mean Average Percentage error and Root mean square error 
is same as of classic Linear Regression model. So tuning the parameters is not helping in 
this case. As I tried also applying cross validation technique, but it is not helping 
either in improving the accuracy. Also, tried to apply model on less number of attributes
but accuracy is decreased further.

2. Ridge Regression Model 
**Construction:** 
This is one of the regularization technique used to simplify the model and reduce
overfitting in our existing Linear Regression model. Here we add an extra term to 
existing loss function and change the value using learning rate(alpha).
**Evaluation:** 
In our given dataset as value of Mean Average Percentage error and Root mean square error 
is almost same for the ridge regression. It means that there is no overfitting in our simple
regression model. Also, as the most of the values are standardize means are having its value
between zero and 100, so also the standardizing the variable is also not improving the
accuracy.Apart from this, also tried to apply on less number of attributes(removing attributes
that I think has less impact) but it further decreased the accuracy.

3. Lasso Regression Model 
**Construction:** 
As we all know that Lasso is the modification of the linear regression and ridge regression.
Here absolute values of the coefficient can be reduced and many will tend to zero in this process. 
In our previous linear regression model we found the coefficient of each attribute
used in training. Here in this it selects the coefficients with higher values and 
eliminates those not having strong relationship( by making those attributes coefficients zero).
**Evaluation**
In the given dataset, it has been found that using this method increased the Mean
Average Percentage error and Root mean square error with respect to linear regression.
This means that regularized model is not better than standard model.
This also tells us that making the model simpler is impacting the accuracy thus
we cannot eliminate the variables/attributes not showing strong relationship.

## Best Model
Linear Regression Model and Grid Search CV Linear Regression Model
(Both showing almost same accuracy)
