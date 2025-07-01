{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1132fcb5-43f6-4c15-a2b9-3e881c078bf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bitcoin Free-Float Market Cap: $769,230,769,230.77\n"
     ]
    }
   ],
   "source": [
    "# S&P Global Free-Float Calculator\n",
    "def calculate_free_float_mcap(total_supply, lost_coins, institutional_hold, market_cap):\n",
    "    \"\"\"\n",
    "    Calculates free-float market cap per S&P methodology\n",
    "    \n",
    "    Parameters:\n",
    "    total_supply (float): Total coins in circulation\n",
    "    lost_coins (float): Permanently inaccessible coins\n",
    "    institutional_hold (float): Long-term locked coins\n",
    "    market_cap (float): Total market capitalization\n",
    "    \n",
    "    Returns:\n",
    "    float: Free-float adjusted market cap\n",
    "    \"\"\"\n",
    "    tradable = total_supply - lost_coins - institutional_hold\n",
    "    factor = tradable / total_supply\n",
    "    return market_cap * factor\n",
    "\n",
    "# Example usage:\n",
    "if __name__ == \"__main__\":\n",
    "    btc_ff = calculate_free_float_mcap(\n",
    "        total_supply=19_500_000,\n",
    "        lost_coins=4_000_000,\n",
    "        institutional_hold=3_000_000,\n",
    "        market_cap=1_200_000_000_000\n",
    "    )\n",
    "    print(f\"Bitcoin Free-Float Market Cap: ${btc_ff:,.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27b44e1a-e3a8-4e7a-90ca-c7fd3bbcb10e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
