The chi-square test is a statistical test that determines if there is a significant association between two categorical variables in a sample. It is used in various fields, including biology, marketing, social sciences, and more, for tasks such as testing independence, homogeneity, and goodness of fit.

### Types of Chi-Square Tests

1. **Chi-Square Test of Independence**: It tests whether two categorical variables are independent of each other or not. It is often used with contingency tables.

2. **Chi-Square Test of Homogeneity**: It tests whether different samples have the same distribution of a categorical variable.

3. **Chi-Square Goodness of Fit Test**: It tests whether the observed sample distribution fits a given theoretical distribution.

### How It Works

The chi-square statistic is calculated as

\[
X^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
\]

where:
- \(X^2\): Chi-square statistic
- \(O_{ij}\): Observed frequency
- \(E_{ij}\): Expected frequency if variables are independent

### Example

Let's take an example where we want to test the independence between two categorical variables: Gender (Male, Female) and Preference (Tea, Coffee).

Here is the observed data in a contingency table:

|         | Tea | Coffee | Total |
|---------|-----|--------|-------|
| Male    | 30  | 10     | 40    |
| Female  | 5   | 45     | 50    |
| Total   | 35  | 55     | 90    |

We will calculate the expected frequencies under the assumption that Gender and Preference are independent, and then use the chi-square formula to calculate the chi-square statistic.

### Calculation

The expected frequency for each cell is calculated as

\[
E_{ij} = \frac{{\text{{row total}} \times \text{{column total}}}}{\text{{grand total}}}
\]

For example, for Male-Tea, the expected frequency is \( \frac{{40 \times 35}}{90} = 15.56 \).

We'll compute the chi-square statistic using the formula above.

Let's calculate it.

### Results

With a p-value of \(1.30 \times 10^{-9}\), which is less than the common alpha level of 0.05, we reject the null hypothesis that gender and preference are independent. This means there is a significant association between gender and preference for tea or coffee in the sample data.

### References

1. Agresti, A. (2007). An Introduction to Categorical Data Analysis (2nd ed.). Wiley-Interscience. 
   - This book provides a comprehensive introduction to methods for categorical data analysis, including the chi-square test.

2. McDonald, J.H. (2014). Handbook of Biological Statistics (3rd ed.). Sparky House Publishing.
   - This handbook is a practical guide to statistical methods for analyzing biological data, with a section dedicated to the chi-square test.

### Note

Remember, the chi-square test has some assumptions, such as the expectation that no cell in the table has an expected count less than 5. It is always essential to check these assumptions before interpreting the results.

I hope this helps! Let me know if you have further questions or need additional clarification on any points.

