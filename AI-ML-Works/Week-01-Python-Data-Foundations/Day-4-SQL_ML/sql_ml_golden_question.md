text
# SQL 1 – Per-sale spend with user total

Query that shows every single sale, and adds a column `user_total_spend` that shows the total spend for that specific user.

SELECT
user_id,
sale_date,
amount,
SUM(amount) OVER (PARTITION BY user_id) AS user_total_spend
FROM sales;

text

---

# SQL 2 – Customer age for retention tracking

Calculate customer age (how many days passed between their first purchase and the current purchase):

- `first_purchase_date`  
- `current_purchase_date`

DATEDIFF(day, first_purchase_date, current_purchase_date)

text

Example query:

SELECT
*,
DATEDIFF(day, first_purchase_date, current_purchase_date) AS customer_age
FROM sales;

text

### Why this feature is useful in models

- Customer age is often the #1 predictor for churn; a customer who has been with you for 500 days is statistically much less likely to quit than someone who joined 2 days ago.  
- Enables cohort analysis: by calculating this value, you can group users into age buckets and see whether 30‑day retention is improving over time.