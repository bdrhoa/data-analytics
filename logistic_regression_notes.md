
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

