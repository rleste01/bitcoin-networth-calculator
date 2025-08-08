# Bitcoin World Wealth Percentile Calculator

Calculate how much Bitcoin you would need to maintain your current wealth percentile if Bitcoin became the world's only store of value.

## 🎯 Overview

This calculator projects Bitcoin requirements based on the thought experiment: "What if Bitcoin ate all global wealth and fiat currency became worthless?" It uses real wealth distribution data to determine how much BTC you'd need to maintain your current economic position.

## 📊 Data Sources

### Global Wealth Distribution (Default)
- **Source**: UBS Global Wealth Report 2024 (official data)
- **Sample**: 3.767 billion adults worldwide
- **Total Wealth**: $449.9 trillion
- **Key Thresholds**:
  - Top 1.5%: $1,000,000+
  - Top 17.8%: $100,000+
  - Bottom 39.5%: Under $10,000
  - Estimated Global Median: ~$25,000

### US Wealth Distribution
- **Source**: Federal Reserve Survey of Consumer Finances (SCF)
- **Sample**: US households only
- **Key Thresholds**:
  - Top 1%: $11,100,000+
  - Top 10%: $1,200,000+
  - Top 25%: $403,000+
  - US Median: $121,000

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install pandas numpy matplotlib
```

### Running the Calculator
```bash
python bitcoin_calculator.py
```

## 📖 How to Use

### Commands
| Command | Description |
|---------|-------------|
| `[number]` | Calculate Bitcoin needed for that net worth (e.g., `250000`) |
| `global` | Switch to global wealth distribution |
| `us` | Switch to US wealth distribution |
| `table` | Show Bitcoin requirements by percentile |
| `plot` | Display visualization |
| `quit` | Exit the calculator |

### Example Session
```
=== Bitcoin World Wealth Percentile Calculator ===

Global Wealth: $449.9 trillion
Bitcoin Supply: 21 million BTC
BTC Price (hyperbitcoinization): $21,424,762

Input: 100000

=== Results for $100,000 (Global (UBS 2024)) ===
Global percentile: 82.20%
Bitcoin needed: 0.00466667 BTC
% of Bitcoin supply: 0.002222%
% of global wealth: 0.00002222%

Input: us

✓ Switched to US wealth distribution (Federal Reserve)
Key thresholds: Top 1%: $11.1M+ | Top 10%: $1.2M+ | Median: $121K

Input: 100000

=== Results for $100,000 (US (Fed SCF)) ===
US percentile: 46.80%
Bitcoin needed: 0.00466667 BTC
% of Bitcoin supply: 0.002222%
% of global wealth: 0.00002222%
```

## 🧮 Core Assumptions

### Hyperbitcoinization Scenario
- **Total Bitcoin Supply**: 21 million BTC (fixed cap)
- **Global Wealth Absorbed**: $449.9 trillion
- **Resulting BTC Price**: ~$21.4 million per Bitcoin
- **Fiat Currency**: Becomes worthless
- **Wealth Distribution**: Maintains current relative positions

### Calculation Method
```
Bitcoin Needed = Your Net Worth ÷ BTC Price
BTC Price = Global Wealth ÷ 21 Million BTC
```

## 📈 Key Insights

### Global vs US Comparison
- **$100K globally**: 82nd percentile (top 18%)
- **$100K in US**: 47th percentile (below median)
- **$1M globally**: 98.5th percentile (top 1.5%)
- **$1M in US**: 90th percentile (top 10%)

### Bitcoin Requirements by Wealth Level
| Net Worth | Global Percentile | Bitcoin Needed | % of Supply |
|-----------|------------------|----------------|-------------|
| $10,000 | 39.5% | 0.00046667 | 0.000222% |
| $25,000 | ~50% | 0.00116667 | 0.000556% |
| $100,000 | 82.2% | 0.00466667 | 0.002222% |
| $1,000,000 | 98.5% | 0.04666667 | 0.022222% |

## 🔬 Methodology

### Data Processing
1. **UBS Wealth Pyramid**: Used actual 2024 wealth distribution bands
2. **Interpolation**: Linear interpolation between known percentile points
3. **Precision**: Extended decimal places to show meaningful Bitcoin percentages
4. **Validation**: Cross-referenced with Federal Reserve US data

### Limitations
- Assumes wealth distribution shape remains constant
- Doesn't account for Bitcoin lost/inaccessible
- Theoretical scenario for educational purposes
- Real hyperbitcoinization would likely have different dynamics

## 📚 References

### Primary Sources
- **UBS Global Wealth Report 2024**: Official global wealth distribution data
- **Federal Reserve SCF**: US household wealth statistics
- **Bitcoin Protocol**: 21 million BTC hard cap

### Wealth Distribution Papers
- Davies, J., Lluberas, R., & Shorrocks, A. (2024). *Global Wealth Report 2024*. UBS.
- Federal Reserve. *Survey of Consumer Finances*. Various years.

## ⚖️ Disclaimer

This calculator is for educational and entertainment purposes only. It represents a theoretical thought experiment and should not be considered financial advice. Real-world hyperbitcoinization would involve complex economic dynamics not modeled here.

- Bug fixes and optimizations

---

*"Fix the money, fix the world."* - Bitcoin community saying
