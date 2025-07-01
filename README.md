# S&P-Style Crypto Index Engine  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Quant Research](https://img.shields.io/badge/Field-Quant_Finance-blue)](https://www.spglobal.com/spdji/en/index-family/cryptocurrency/)  

Professional cryptocurrency index builder replicating S&P Global methodologies.  

## Index Composition  
![S&P Crypto Index](reports/snp_crypto_index.png)  

## Features  
- Free-float adjusted market cap weighting  
- Liquidity screening ($1M+ daily volume)  
- Automated daily reports  
- Anomaly detection integration  

## Usage  
```bash  
# Install dependencies  
pip install -r requirements.txt  

# Run index engine  
jupyter notebook notebooks/s&p_crypto_index.ipynb  
