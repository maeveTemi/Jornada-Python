# Python Customer Churn Analysis

## Overview

This project analyzes customer churn for a company with more than 800,000 customers.

The company identified that a large portion of its customer base had become inactive and wanted to understand the main patterns associated with cancellations, as well as identify actions that could potentially help reduce churn.

The analysis was developed in Python as part of the **Python Insights - Analisando Dados com Python** project.

## Business Problem

The company wanted to answer two main questions:

- How many customers are cancelling their services?
- What characteristics or behaviors are most associated with customer cancellations?

Based on the analysis, the goal was to identify actionable patterns that could support strategies for reducing churn.

## Technologies Used

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Data analysis and processing   |
| pandas           | Data manipulation and cleaning |
| Plotly           | Data visualization             |
| Jupyter Notebook | Analysis environment           |

## Project Workflow

The project followed these main steps:

1. Import the customer database
2. Explore the available data
3. Clean and prepare the dataset
4. Analyze the overall cancellation rate
5. Investigate patterns associated with customer cancellations
6. Apply potential retention criteria and compare the results

## Data Cleaning

Before analyzing the data, I performed some basic data preparation.

### Customer ID

The `CustomerID` column was removed because it is an identifier and does not provide useful information for the analysis.

```python
table = table.drop(columns="CustomerID")
```

### Missing Values

The dataset contained 5 rows with missing information. These records were removed before continuing with the analysis.

```python
table = table.dropna()
```

The dataset was also inspected using `info()` to verify the data types and identify missing values.

## Initial Analysis

The first analysis focused on understanding the overall distribution of customer cancellations.

```python
table["cancelou"].value_counts()
```

The cancellation rate was then calculated using normalized values:

```python
table["cancelou"].value_counts(normalize=True)
```

The initial analysis showed a **56% cancellation rate** in the dataset.

## Cancellation Analysis

To investigate the characteristics associated with churn, I created histograms comparing different customer attributes against the `cancelou` variable.

```python
import plotly.express as px

for column in table.columns:
    graph = px.histogram(table, x=column, color="cancelou")
    graph.show()
```

This allowed me to visually compare cancellation patterns across different variables.

### Main Findings

The analysis highlighted three particularly relevant patterns:

#### Contract Duration

Customers on monthly contracts showed a strong concentration of cancellations.

**Potential action:** encourage customers to move to longer-term contracts by offering incentives for annual or quarterly plans.

#### Call Center Interactions

Customers with more than 4 call center interactions showed a very high concentration of cancellations.

**Potential action:** create an early-warning system for customers who contact the call center repeatedly, allowing the company to investigate unresolved issues before the customer cancels.

#### Payment Delays

Customers with payment delays above 20 days showed a strong association with cancellations.

**Potential action:** create an alert for customers whose payment delays exceed a defined threshold, allowing the company to intervene before the customer churns.

## Retention Simulation

After identifying these patterns, I applied a set of filters to simulate a potential customer-retention strategy.

The criteria were:

- Contract duration different from `Monthly`
- 4 or fewer call center interactions
- 20 or fewer days of payment delay

```python
condition = table["duracao_contrato"] != "Monthly"
table = table[condition]

condition = table["ligacoes_callcenter"] <= 4
table = table[condition]

condition = table["dias_atraso"] <= 20
table = table[condition]
```

Finally, I recalculated the cancellation rate:

```python
table["cancelou"].value_counts(normalize=True)
```

This provides a simple way to evaluate how the customer profile changes when these potentially high-risk characteristics are excluded.

## Key Takeaways

The analysis demonstrated how exploratory data analysis can help identify patterns within a large customer database.

The most relevant patterns identified were:

- Monthly contracts were strongly associated with cancellations.
- A high number of call center interactions was associated with a higher concentration of cancellations.
- Longer payment delays were associated with increased cancellations.
- These patterns can be translated into potential retention strategies and early-warning indicators.

These findings represent **associations observed in the dataset and not proof of causation**. Further analysis would be necessary to determine the underlying causes and estimate the potential impact of each intervention.

## What I Learned

Through this project, I practiced:

- Importing and exploring datasets with pandas
- Identifying and handling missing values
- Removing irrelevant columns
- Calculating frequencies and percentages
- Using conditional filtering in pandas
- Creating interactive visualizations with Plotly
- Exploring relationships between customer characteristics and churn
- Translating data patterns into potential business actions
- Thinking about data analysis from a business perspective

## Possible Improvements

Some possible next steps for this analysis include:

- Calculate the cancellation rate for each individual customer segment instead of relying only on histograms.
- Investigate whether the identified variables remain significant when analyzed together.
- Create a dashboard to make the findings easier to communicate.
- Develop a customer churn prediction model.
- Identify additional variables that may explain cancellations.
- Quantify the potential financial impact of different retention strategies.

## Project Context

This project was developed as part of the **Python Insights - Analisando Dados com Python** course/project.

It was created as a practical exercise in Python-based data analysis, with a focus on transforming a business problem into an exploratory data analysis workflow.
