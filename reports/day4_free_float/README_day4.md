# Day 4: Free-Float Mastery  
## Concepts Learned  
- Free-float = Only tradable coins/shares  
- S&P calculation: `(Circulating Supply - Locked Coins) / Circulating Supply`  
- Why it matters: Prevents index manipulation  

## Professional Implementation  
```python
def calculate_free_float_mcap(total_supply, lost_coins, institutional_hold, market_cap):
    tradable = total_supply - lost_coins - institutional_hold
    factor = tradable / total_supply
    return market_cap * factor
