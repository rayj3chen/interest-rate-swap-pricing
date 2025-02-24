import QuantLib as ql
import matplotlib.pyplot as plt

# Step 1: Set the evaluation date
today = ql.Date(15, 10, 2023)
ql.Settings.instance().evaluationDate = today

# Step 2: Define the swap parameters
notional = 1000000  # Notional amount
fixed_rate = 0.03  # Fixed rate (3%)
floating_spread = 0.0  # Spread over the floating rate index
tenor = ql.Period(2, ql.Years)  # Swap tenor (2 years)
fixed_leg_tenor = ql.Period(6, ql.Months)  # Fixed leg payment frequency (semi-annual)
floating_leg_tenor = ql.Period(3, ql.Months)  # Floating leg payment frequency (quarterly)
calendar = ql.UnitedStates()  # Calendar for business days
business_convention = ql.ModifiedFollowing  # Business day convention
day_count = ql.Thirty360()  # Day count convention

# Step 3: Create the floating rate index (e.g., 6-month LIBOR)
index = ql.Euribor6M()

# Step 4: Create the swap
swap = ql.VanillaSwap(
    ql.VanillaSwap.Payer,  # Payer of the fixed rate
    notional,  # Notional amount
    today + tenor,  # Maturity date
    fixed_rate,  # Fixed rate
    day_count,  # Fixed leg day count
    index,  # Floating rate index
    floating_spread,  # Floating rate spread
    day_count,  # Floating leg day count
    calendar,  # Calendar
    business_convention,  # Business day convention
    business_convention  # Business day convention
)

# Step 5: Create a discount curve (flat yield curve for simplicity)
flat_rate = 0.02  # Flat discount rate (2%)
flat_curve = ql.FlatForward(today, flat_rate, day_count, ql.Continuous)
discount_curve = ql.YieldTermStructureHandle(flat_curve)

# Step 6: Set the pricing engine for the swap
swap.setPricingEngine(ql.DiscountingSwapEngine(discount_curve))

# Step 7: Calculate the NPV of the swap
npv = swap.NPV()
print(f"Swap NPV: {npv:.2f}")

# Step 8: Analyze the fixed and floating legs
fixed_leg_npv = swap.fixedLegNPV()
floating_leg_npv = swap.floatingLegNPV()
print(f"Fixed Leg NPV: {fixed_leg_npv:.2f}")
print(f"Floating Leg NPV: {floating_leg_npv:.2f}")

# Step 9: Visualize the yield curve
dates = [today + ql.Period(i, ql.Months) for i in range(0, 25)]
rates = [flat_curve.zeroRate(d, day_count, ql.Continuous).rate() for d in dates]

plt.plot(dates, rates, label="Yield Curve")
plt.title("Flat Yield Curve")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.legend()
plt.show()
