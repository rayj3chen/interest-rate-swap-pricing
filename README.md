# Interest Rate Swap Pricing with QuantLib

This project demonstrates how to price an **interest rate swap** using the **QuantLib** library in Python. It includes the calculation of the Net Present Value (NPV) of the swap, analysis of the fixed and floating legs, and visualization of the yield curve.

---

## Overview

An **interest rate swap** is a financial derivative in which two parties agree to exchange interest payments based on a specified notional amount. This project uses the **QuantLib** library to:
- Define the terms of the swap.
- Create a yield curve for discounting cash flows.
- Calculate the NPV of the swap.
- Visualize the yield curve.

---

## Explanation of the Code

The project consists of a single Python script (swap_pricing.py) with the following structure:

- Evaluation Date: The today variable sets the current date for pricing the swap.

- Swap Parameters: The swap is defined with a notional amount, fixed rate, floating rate index, and payment frequencies.

- Floating Rate Index: The floating rate is tied to a benchmark.

- Discount Curve: A flat yield curve is used for discounting cash flows. In practice, you might use a more sophisticated curve (e.g., bootstrapped from market data).

- Pricing Engine: The DiscountingSwapEngine calculates the NPV of the swap by discounting the fixed and floating cash flows.

- NPV Calculation: The NPV of the swap is the difference between the present value of the fixed leg and the floating leg.

- Visualization: The yield curve is plotted using matplotlib (optional).

## Requirements

To run this project, you need the following Python libraries:
- **QuantLib**: For financial calculations.
- **matplotlib**: For visualizing the yield curve (optional).
