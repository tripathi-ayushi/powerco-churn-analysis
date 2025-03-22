# 📘 Story-Based Report: Is Price Sensitivity Driving Churn at PowerCo?

As a Data Scientist embedded in a BCG engagement simulation with **PowerCo**, a leading energy provider, I was given a crucial mission: uncover the real reason behind customer churn.

The executive team believed that **price sensitivity** — how customers react to energy pricing — was the primary reason clients were leaving. My role? Put that theory to the test using data.

---

## 🔬 What I Did

I started by performing a thorough **exploratory data analysis (EDA)** to understand consumption patterns, pricing trends, and customer behaviors. Then I engineered features that could represent **price sensitivity**, such as:

- Cost per unit of energy (peak and off-peak)
- Spread between peak and off-peak pricing
- A ratio comparing pricing to customer value
- A composite "price sensitivity score"

These features were fed into a machine learning model (Random Forest) to predict whether a customer would churn.

---

## 📊 What I Found

While the model performed reasonably well on accuracy (~88%), its **AUC score was only 0.545**, suggesting that **price-based features alone don't explain churn effectively**.

The **feature importance plot** confirmed that while price sensitivity had some influence, **it was not the most dominant signal**.

---

## 🧠 Final Insight

> ❌ **Price sensitivity is not the main factor driving customer churn.**

This suggests customers may be leaving due to:
- Poor service experiences
- Better offers from competitors
- Contract terms or renewal timing
- Lack of engagement or value perception

---

## ✅ Recommendation

Future models should incorporate:
- Customer tenure and lifecycle stage
- Behavioral features like product switches or service complaints
- Time-based usage trends and seasonality
- Loyalty or engagement metrics

By blending price with behavioral data, we can better understand and predict why customers leave — and most importantly, how to retain them.

---

**Project completed as part of the [BCG x Forage Virtual Internship Program](https://www.theforage.com/).**
