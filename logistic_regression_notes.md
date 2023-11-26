Logistic Regression Notes
Brad Rhoads
11/25/202

When comparing a binary, categorical variable like ReAdmis to other variables, the approach is somewhat different from comparing continuous variables. This is because the statistical methods used for categorical data analysis differ from those used for continuous data.

Here's what you should consider:

For Numeric Variables: Instead of correlation, you would typically use a t-test or Mann-Whitney U test (non-parametric alternative) to compare the means of the two groups defined by the binary variable.

For Categorical Variables: If you are comparing two categorical variables, you can use a Chi-squared test or Fisher's exact test to look for associations between the levels of the two variables.

Here's how you could modify your R code:

```
for (col_name in names(data)) {
  
  # Skip if the variable is ReAdmis itself
  if (col_name == "ReAdmis") {
    next
  }
  
  cat("For ReAdmis and", col_name, ":\n")
  
  # Check datatype
  if (is.factor(data[[col_name]])) {
    # For factor variables
    cat("Table of counts for levels of", col_name, "by ReAdmis:\n")
    table_of_counts <- table(data$ReAdmis, data[[col_name]])
    print(table_of_counts)
    
    cat("Chi-squared Test for association between ReAdmis and", col_name, ":\n")
    chi_squared_test <- chisq.test(table_of_counts)
    print(chi_squared_test)
    
  } else if (is.numeric(data[[col_name]])) {
    # For numeric variables
    cat("Mean of", col_name, "by ReAdmis levels:\n")
    mean_by_ReAdmis <- tapply(data[[col_name]], data$ReAdmis, mean, na.rm = TRUE)
    print(round(mean_by_ReAdmis, 2))
    
    cat("T-test for difference in means of", col_name, "by ReAdmis levels:\n")
    t_test <- t.test(data[[col_name]] ~ data$ReAdmis)
    print(t_test)
    
  } else {
    # If other datatype, print message and skip
    cat("Unknown data type for", col_name, "- skipping.\n")
    next
  }
  
  cat("\n------------------------\n")
}
```

To visualize the comparisons between a binary variable like ReAdmis and other variables in your dataset, you can use a variety of plots. For numeric variables, boxplots or violin plots are commonly used, while for categorical variables, bar plots or mosaic plots can be helpful.

Here's an example of how you might modify your R code to include visualizations:

```
library(ggplot2)

for (col_name in names(data)) {
  
  # Skip if the variable is ReAdmis itself
  if (col_name == "ReAdmis") {
    next
  }
  
  cat("For ReAdmis and", col_name, ":\n")
  
  # Check datatype
  if (is.factor(data[[col_name]])) {
    # For factor variables
    cat("Bar plot for levels of", col_name, "by ReAdmis:\n")
    plot <- ggplot(data, aes(x=!!sym(col_name), fill=!!sym("ReAdmis"))) +
      geom_bar(position="dodge") +
      labs(title=paste("Bar plot of", col_name, "by ReAdmis levels"), x=col_name, fill="ReAdmis") +
      theme_minimal()
    print(plot)
    ggsave(filename=paste("Barplot_", col_name, "_by_ReAdmis.png", sep=""), plot=plot, width=8, height=6, dpi=300)
    
  } else if (is.numeric(data[[col_name]])) {
    # For numeric variables
    cat("Boxplot of", col_name, "by ReAdmis levels:\n")
    plot <- ggplot(data, aes(x=factor(ReAdmis), y=!!sym(col_name), fill=factor(ReAdmis))) +
      geom_boxplot() +
      labs(title=paste("Boxplot of", col_name, "by ReAdmis levels"), x="ReAdmis", y=col_name) +
      theme_minimal()
    print(plot)
    ggsave(filename=paste("Boxplot_", col_name, "_by_ReAdmis.png", sep=""), plot=plot, width=8, height=6, dpi=300)
    
    cat("Violin plot of", col_name, "by ReAdmis levels:\n")
    plot <- ggplot(data, aes(x=factor(ReAdmis), y=!!sym(col_name), fill=factor(ReAdmis))) +
      geom_violin(trim=FALSE) +
      labs(title=paste("Violin plot of", col_name, "by ReAdmis levels"), x="ReAdmis", y=col_name) +
      theme_minimal()
    print(plot)
    ggsave(filename=paste("Violin_", col_name, "_by_ReAdmis.png", sep=""), plot=plot, width=8, height=6, dpi=300)
    
  } else {
    # If other datatype, print message and skip
    cat("Unknown data type for", col_name, "- skipping.\n")
    next
  }
  
  cat("\n------------------------\n")
}
```
CONFUSION MATRIX

```
# Load necessary libraries
library(ggplot2)
library(caret)
library(reshape2)

# Actual and predicted data (as before)
actual <- factor(c('Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes'))
predicted <- factor(c('Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes'))

# Create the confusion matrix
conf_matrix <- table(Predicted = predicted, Actual = actual)

# Melt the confusion matrix
melted_conf_matrix <- melt(conf_matrix)

# Plot the heatmap
ggplot(data = melted_conf_matrix, aes(x = Actual, y = Predicted, fill = value)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") +
  geom_text(aes(label = value), vjust = 1) +
  labs(x = "Actual", y = "Predicted", fill = "Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

```

VISUALIZATIONS

```
install.packages(c("ggplot2", "vcd", "graphics", "reshape2"))
library(ggplot2)
library(vcd)
library(graphics)
library(reshape2)

# Sample confusion matrix
conf_matrix <- matrix(c(50, 10, 5, 35), nrow = 2, byrow = TRUE)
dimnames(conf_matrix) <- list(Predicted = c("Positive", "Negative"), 
                              Actual = c("Positive", "Negative"))

```
Heatmap
```
# Melting the matrix for ggplot
melted_conf_matrix <- melt(conf_matrix)

# Plotting the heatmap
ggplot(data = melted_conf_matrix, aes(x = Actual, y = Predicted, fill = value)) +
  geom_tile() +
  geom_text(aes(label = value), vjust = 1) +
  scale_fill_gradient(low = "white", high = "blue") +
  labs(x = "Actual", y = "Predicted", fill = "Count") +
  theme_minimal()

```
Fourfold Plot
```
# Melting the matrix for ggplot
melted_conf_matrix <- melt(conf_matrix)

# Plotting the heatmap
ggplot(data = melted_conf_matrix, aes(x = Actual, y = Predicted, fill = value)) +
  geom_tile() +
  geom_text(aes(label = value), vjust = 1) +
  scale_fill_gradient(low = "white", high = "blue") +
  labs(x = "Actual", y = "Predicted", fill = "Count") +
  theme_minimal()

```
Mosaic Plot
```
# Mosaic plot
mosaicplot(conf_matrix, main = "Mosaic Plot of Confusion Matrix")

```
Bar Chart
```
# Bar plot
barplot(as.matrix(conf_matrix), beside = TRUE, legend = rownames(conf_matrix),
        args.legend = list(x = "topright"), col = c("lightblue", "salmon"),
        xlab = "Actual", ylab = "Count", ylim = c(0, max(conf_matrix) * 1.5))

```
TESTING LOGISTIC REGRESSION ASSUMPTIONS
```
# Enhanced function to test logistic regression assumptions with scope correction
test_logistic_regression_assumptions <- function(data, dependent_var, independent_vars) {
  
  # 1. Check if dependent variable is binary
  binary_check <- length(unique(data[[dependent_var]])) == 2
  cat("1. Binary Outcome Variable Check: ", ifelse(binary_check, "Passed", "Failed"), "\n")
  
  # 2. Independence of observations (Not directly testable; requires domain knowledge)
  cat("2. Independence of Observations: Manual check required\n")

  # Define full_model outside the if block
  full_model <- as.formula(paste(dependent_var, "~", paste(independent_vars, collapse = "+")))

  # 3. Test for linearity of independent variables and log odds
  positive_vars <- independent_vars[sapply(data[independent_vars], function(x) all(x > 0))]
  if (length(positive_vars) > 0) {
    pos_full_model <- as.formula(paste(dependent_var, "~", paste(positive_vars, collapse = "+")))
    box_tidwell_test <- boxTidwell(pos_full_model, ~., data = data)
    linearity_check <- all(box_tidwell_test$p.value > 0.05)
    cat("3. Linearity of Independent Variables and Log Odds (for positive variables only): ", ifelse(linearity_check, "Passed", "Failed"), "\n")
  } else {
    cat("3. Linearity of Independent Variables and Log Odds: Not testable (no positive variables)\n")
  }

  # 4. Check for multicollinearity
  model <- glm(full_model, family = "binomial", data = data)
  vif_values <- vif(model)
  multicollinearity_check <- all(vif_values < 10)
  cat("4. No Multicollinearity: ", ifelse(multicollinearity_check, "Passed", "Failed"), "\n")

  # 5. Check for significant outliers
  cooks_dist <- cooks.distance(model)
  outliers_check <- all(cooks_dist < 4/(nrow(data)-length(independent_vars)-2))
  cat("5. No Significant Outliers: ", ifelse(outliers_check, "Passed", "Failed"), "\n")

  # 6. Sample size check using the rule of thumb
  least_frequent_outcome_prob <- min(mean(data[[dependent_var]]), 1 - mean(data[[dependent_var]]))
  required_sample_size <- (10 * length(independent_vars)) / least_frequent_outcome_prob
  sample_size_check <- nrow(data) >= required_sample_size
  cat("6. Adequate Sample Size: ", ifelse(sample_size_check, "Passed", "Failed"), "\n")
}

# Demonstration using a hypothetical dataset
# Generating a sample dataset
set.seed(123) # For reproducibility
my_data <- data.frame(
  Outcome = sample(c(0, 1), 200, replace = TRUE), # Binary outcome
  Var1 = rnorm(200) + 1, # Ensuring positive values
  Var2 = rnorm(200) + 1,
  Var3 = rnorm(200) + 1
)

# Using the function on the sample dataset
test_logistic_regression_assumptions(my_data, "Outcome", c("Var1", "Var2", "Var3"))

```
COOKS DISTANCE

Cook's Distance and Tukey's method are both used for detecting outliers, but they approach the problem in different ways and can have different impacts when applied to logistic regression models.

Cook's Distance
Definition: Cook's Distance measures the influence of each observation on the fitted values of a regression model. It's based on the changes in the estimated coefficients when an observation is removed.
Use in Logistic Regression:
It evaluates the effect of deleting a data point on the model as a whole.
Useful in identifying points that might be unduly influencing the model parameters.
Particularly helpful in assessing the robustness of the model.
Impact: An observation with a large Cook’s distance might be an outlier or have a high leverage, indicating it significantly changes the model's outcome.
Tukey's Method (Box Plot Rule)
Definition: Tukey's method, often applied using a box plot, identifies outliers based on the interquartile range (IQR). Observations are flagged as outliers if they fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR.
Use in Logistic Regression:
It is more focused on identifying extreme values in the data rather than their influence on the model.
Can be used as a preliminary step before modeling to clean the data.
Less about the influence on parameters and more about identifying individual extreme data points.
Impact: Helps in removing extreme values that might skew the distribution of data, which is important for logistic regression assumptions.
Comparison and Suitability
Sensitivity: Cook's Distance is more sensitive to points that have a large influence on the regression coefficients, whereas Tukey's method is focused on identifying extreme values based on a fixed rule.
Approach: Cook's Distance is model-dependent and assesses the impact of points on the model. Tukey's method is a univariate method and doesn’t take into account the model.
Applicability to Logistic Regression: Cook's Distance might be more appropriate for logistic regression as it directly assesses the impact on the model. However, Tukey's method is still useful for initial data screening.
Conclusion
Finding Extreme Outliers: Tukey's method is more straightforward and rule-based, ideal for quickly flagging extreme values.
Assessing Impact on Model: Cook's Distance provides insight into how much an observation is influencing the model's parameters, which is crucial in regression analysis.
In practice, using both methods in tandem can be beneficial: Tukey's method for initial data cleaning and Cook's Distance for assessing the influence of observations on the logistic regression model.
```
# Sample data
set.seed(123) # for reproducibility
x <- runif(100, min = 0, max = 100) # 100 random numbers
y <- ifelse(x + rnorm(100) > 50, 1, 0) # binary outcome
data <- data.frame(x, y)

# Logistic regression
model <- glm(y ~ x, data = data, family = "binomial")

# Cook's distance
cooks.distances <- cooks.distance(model)

# Threshold for influential points
threshold <- 4 / length(cooks.distances)

# Influential observations
influential <- which(cooks.distances > threshold)

# Plotting
plot(cooks.distances, pch = 20, type = "h", main = "Cook's Distance", ylab = "Cook's Distance")
abline(h = threshold, col = "red", lty = 2)
points(influential, cooks.distances[influential], col = "blue", pch = 4)

# Assuming 'influential_points' contains the indexes of influential observations
data_clean <- data[-influential_points, ]

#After removing these rows, you may want to reset the row names if they are no longer sequential:
# Reset row names
row.names(data_clean) <- NULL
```
LOGISTIC ACCURACY
```
# Assuming you have a dataset `data` with predictors and a binary response variable `outcome`

# Split the data into training and test sets (e.g., 70% training, 30% test)
set.seed(123) # for reproducibility
training_indices <- sample(1:nrow(data), 0.7 * nrow(data))
train_data <- data[training_indices, ]
test_data <- data[-training_indices, ]

# Fit logistic regression model
model <- glm(outcome ~ ., data = train_data, family = "binomial")

# Predict on test data
predictions_prob <- predict(model, test_data, type = "response")
predictions <- ifelse(predictions_prob > 0.5, 1, 0)

# Calculate accuracy
actual <- test_data$outcome
accuracy <- sum(predictions == actual) / length(actual)

print(accuracy)

```
RECODE GENDER TO MODE
```
# Your dataset
# df <- ...

# Function to calculate mode
get_mode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

# Calculate mode for gender excluding 'Nonbinary'
mode_gender <- get_mode(df$gender[df$gender != "Nonbinary"])

# Recode 'Nonbinary' to mode gender
df$gender[df$gender == "Nonbinary"] <- mode_gender

```
Logarithms are a fundamental concept in mathematics, particularly useful in solving equations involving exponential terms. Here's a basic explanation:

Definition: A logarithm is the inverse operation to exponentiation. Just as division is the inverse of multiplication, logarithms are the inverse of raising a number to a power. For example, if you have 
2
3
=
8
2 
3
 =8, then you can express this as a logarithm: 
log
⁡
2
8
=
3
log 
2
​
 8=3. This reads as "the logarithm of 8 with base 2 is 3".

Base of a Logarithm: The base of a logarithm is the number that is raised to a power. In the example 
log
⁡
2
8
=
3
log 
2
​
 8=3, the base is 2. Common bases are 10 (common logarithm, denoted as 
log
⁡
log) and 
�
e (natural logarithm, denoted as 
ln
⁡
ln), where 
�
e is an irrational and transcendental number approximately equal to 2.71828.

Calculating Logarithms: The value of a logarithm answers the question: "To what power must the base be raised, to produce this number?" In the example 
log
⁡
2
8
log 
2
​
 8, we are asking "What power must 2 be raised to, to get 8?" and the answer is 3.

Properties of Logarithms:

Product Rule: 
log
⁡
�
(
�
×
�
)
=
log
⁡
�
�
+
log
⁡
�
�
log 
b
​
 (M×N)=log 
b
​
 M+log 
b
​
 N
Quotient Rule: 
log
⁡
�
(
�
�
)
=
log
⁡
�
�
−
log
⁡
�
�
log 
b
​
 ( 
N
M
​
 )=log 
b
​
 M−log 
b
​
 N
Power Rule: 
log
⁡
�
(
�
�
)
=
�
×
log
⁡
�
�
log 
b
​
 (M 
p
 )=p×log 
b
​
 M
Applications: Logarithms are used in many areas including science, engineering, and finance. They are particularly helpful in dealing with exponential growth or decay, such as in population studies, radioactive decay, and interest calculations.

Understanding logarithms can be a bit challenging at first, but they're a powerful tool once you get the hang of them. They essentially allow us to work with very large or very small numbers in a more manageable way and solve equations that would be difficult or impossible to solve using just arithmetic operations.

User
Now explain log(Odds)
Share
Save
ChatGPT
Log odds, often encountered in statistics and probability theory, is a concept that combines the ideas of logarithms and odds. Here's an explanation:

Understanding Odds: Odds are a way of expressing probability. Given an event with a probability 
�
P of occurring, the odds of the event are given as 
�
1
−
�
1−P
P
​
 . In simpler terms, odds compare the probability of an event happening to the probability of it not happening.

Log Odds: Log odds is simply the logarithm of the odds. If the odds are given as 
�
=
�
1
−
�
O= 
1−P
P
​
 , then the log odds are 
log
⁡
(
�
)
log(O). The base of the logarithm can vary, but in many contexts, especially in logistic regression (a statistical method), the natural logarithm is used. This would make the log odds 
ln
⁡
(
�
1
−
�
)
ln( 
1−P
P
​
 ).

Interpretation and Use:

In Statistics: Log odds are a central part of logistic regression, a type of regression analysis used for predicting the outcome of a categorical dependent variable based on one or more predictor variables. The log odds are used as the response variable.
As a Transformation: Converting probabilities to log odds is a way of transforming a variable that can range between 0 and 1 (i.e., probabilities) to a variable that can take any value from negative infinity to positive infinity. This can simplify certain types of statistical analysis and model-building.
Interpreting Values: Positive log odds indicate that an event is more likely to occur than not, and negative log odds indicate that an event is less likely to occur than not. A log odds of 0 indicates that an event is equally likely to occur or not occur (i.e., the event has a 50% probability).
Advantages: One of the main advantages of using log odds is that it can handle situations where the outcome is binary (i.e., it can happen or not happen), which is common in many practical situations. This transformation to log odds makes the relationship between variables more linear and easier to model, especially in logistic regression.

In summary, log odds is a logarithmic transformation of the odds of an event, widely used in statistical modeling and analysis, particularly when dealing with binary outcomes. It helps in interpreting and modeling probabilities in a more mathematically convenient and interpretable format.

User
Tell me more about how log odds are related to logistic regression.
Share
Save
ChatGPT
Log odds play a crucial role in logistic regression, a statistical method used for modeling the probability of a binary outcome. Here's how log odds are related to logistic regression:

Binary Outcomes: Logistic regression is used when the dependent variable is binary—meaning it has only two possible outcomes, often coded as 0 and 1 (e.g., "no" and "yes", "fail" and "pass", "healthy" and "sick").

Modeling Probabilities: The goal of logistic regression is to model the probability that the dependent variable is in a particular category (usually the "1" or "yes" category) based on one or more independent variables.

Logit Function: The logistic regression model uses the logit function, which is the logarithm of the odds of the dependent variable being in a particular category. If 
�
P is the probability of the outcome, the logit function is defined as:

logit
(
�
)
=
ln
⁡
(
�
1
−
�
)
logit(P)=ln( 
1−P
P
​
 )
This is the natural log of the odds, as discussed earlier.

Linear Relationship: The key advantage of using log odds (logit function) in logistic regression is that it creates a linear relationship between the independent variables and the log odds of the dependent variable. The general form of the logistic regression model is:

ln
⁡
(
�
1
−
�
)
=
�
0
+
�
1
�
1
+
�
2
�
2
+
…
+
�
�
�
�
ln( 
1−P
P
​
 )=β 
0
​
 +β 
1
​
 X 
1
​
 +β 
2
​
 X 
2
​
 +…+β 
n
​
 X 
n
​
 
Here, 
�
0
,
�
1
,
…
,
�
�
β 
0
​
 ,β 
1
​
 ,…,β 
n
​
  are the parameters of the model, and 
�
1
,
�
2
,
…
,
�
�
X 
1
​
 ,X 
2
​
 ,…,X 
n
​
  are the independent variables.

Sigmoid Function: The output of the logistic regression model can be transformed back to a probability using the sigmoid function (also known as the logistic function). The sigmoid function is the inverse of the logit function and is given by:

�
(
�
)
=
1
1
+
�
−
�
σ(x)= 
1+e 
−x
 
1
​
 
where 
�
x is the linear combination of independent variables (
�
0
+
�
1
�
1
+
…
+
�
�
�
�
β 
0
​
 +β 
1
​
 X 
1
​
 +…+β 
n
​
 X 
n
​
 ). The sigmoid function maps any real-valued number into the range (0, 1), making it suitable for probability.

Interpretation of Coefficients: In logistic regression, interpreting the coefficients involves understanding the change in log odds. A one-unit increase in an independent variable 
�
�
X 
i
​
  results in a change in the log odds of the dependent variable by 
�
�
β 
i
​
 , holding other variables constant.

Applications: Logistic regression is widely used in various fields, such as medicine (e.g., predicting the likelihood of a disease), finance (e.g., credit scoring), marketing (e.g., predicting customer behavior), and many more areas where predicting binary outcomes is essential.

In summary, logistic regression models the log odds of a binary outcome as a linear combination of independent variables. This approach provides a powerful way to understand the relationships between variables and to predict binary outcomes in various practical scenarios.



References:
https://chat.openai.com/c/5c780ac8-08bb-4a12-989c-07b4f3db3f9f
https://chat.openai.com/c/bd230a8c-5f51-4416-9fd4-2c4eb9f5a73b
https://chat.openai.com/c/1fc14325-7723-4995-8f54-91fbe12cda13
https://chat.openai.com/c/71ed0cca-b400-4076-8b28-95020f91744b
https://chat.openai.com/c/123fc548-16d8-479e-995f-5e11878d38c0
https://chat.openai.com/c/098218aa-5a84-486d-a32a-b98c6d7cfa7f
