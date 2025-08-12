# Bitcoin World Wealth Percentile Calculator

Calculate how much Bitcoin you would need to maintain your current wealth percentile if Bitcoin became the world's only store of value.

## 🎯 Overview

This calculator projects Bitcoin requirements based on the thought experiment: "What if Bitcoin ate all global wealth and fiat currency became worthless?" It uses real wealth distribution data to determine how much BTC you'd need to maintain your current economic position.

## 📊 Data Sources

### Global Wealth Distribution (Default)
- **Source**: UBS Global Wealth Report 2024 (official data)
- **Population**: 3.767 billion adults worldwide
- **Total Wealth**: $449.9 trillion
- **Bitcoin Allocation**: Full 21 million BTC supply
- **Key Thresholds**:
  - Top 1.5%: $1,000,000+
  - Top 17.8%: $100,000+
  - Bottom 39.5%: Under $10,000
  - Global Median: ~$25,000

### US Wealth Distribution
- **Source**: Federal Reserve Survey of Consumer Finances (SCF)
- **Population**: 260 million adults (6.9% of global)
- **Total Wealth**: $135 trillion (30% of global wealth)
- **Bitcoin Allocation**: 6.3 million BTC (proportional 30% share)
- **Key Thresholds**:
  - Top 1%: $11,100,000+
  - Top 10%: $1,200,000+
  - US Median: $121,000

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install pandas numpy matplotlib requests
```

### Running the Calculator
```bash
python3 bitcoin_calculator.py
```

## 📖 How to Use

### Commands
| Command | Description |
|---------|-------------|
| `[number]` | Calculate Bitcoin needed for that net worth (e.g., `250000`) |
| `global` | Switch to global wealth distribution (compete for 21M BTC) |
| `us` | Switch to US wealth distribution (compete for 6.3M BTC) |
| `table` | Show Bitcoin requirements by percentile |
| `plot` | Display visualization |
| `quit` | Exit the calculator |

### Example Session
```
=== Bitcoin World Wealth Percentile Calculator ===

Global: 3.8B adults, $449.9T wealth
US: 260M adults (6.9%), $135.0T wealth (30%)
Bitcoin Supply: 21M total | US allocation: 6.3M
BTC Price (hyperbitcoinization): $21,423,810
Current BTC Price: $67,543

Commands: [number] | 'global' | 'us' | 'table' | 'plot' | 'quit'

Input: 100000

=== Results for $100,000 (Global (UBS 2024)) ===
Global percentile: 82.20%
Bitcoin needed: 0.00466857 BTC
Current cost: $315.42
% of total supply (21M): 0.002223%
% of global wealth: 0.00002223%

Input: us

✓ Switched to US wealth distribution
Population: 260M adults (6.9% of global)
Wealth: $135.0T (30% of global)
Bitcoin: Compete for 6.3M BTC allocation
Thresholds: Top 1%: $11.1M+ | Top 10%: $1.2M+ | Median: $121K

Input: 100000

=== Results for $100,000 (US (Fed SCF)) ===
US percentile: 46.80%
Bitcoin needed: 0.00466857 BTC
Current cost: $315.42
% of US allocation (6.3M): 0.007408%
% of total supply (21M): 0.002223%
% of US wealth: 0.00007408%
% of global wealth: 0.00002223%
```

## 🧮 Core Assumptions

### Hyperbitcoinization Scenario
- **Total Bitcoin Supply**: 21 million BTC (fixed cap)
- **Global Wealth Absorbed**: $449.9 trillion
- **US Wealth Share**: $135 trillion (30% of global)
- **US Bitcoin Allocation**: 6.3 million BTC (proportional to wealth share)
- **Resulting BTC Price**: ~$21.4 million per Bitcoin
- **Fiat Currency**: Becomes worthless
- **Wealth Distribution**: Maintains current relative positions

### Calculation Methods

**Global Mode:**
```
Bitcoin Needed = Your Net Worth ÷ Global BTC Price
Global BTC Price = $449.9T ÷ 21M BTC = $21.4M per BTC
Competition = Against 3.8B people for 21M BTC
```

**US Mode:**
```
Bitcoin Needed = Your Net Worth ÷ US BTC Price  
US BTC Price = $135T ÷ 6.3M BTC = $21.4M per BTC
Competition = Against 260M Americans for 6.3M BTC
```

## 💰 Real-Time Pricing

The calculator fetches current Bitcoin prices from CoinGecko API to show:
- **Current cost** to acquire your calculated Bitcoin amount
- **Reality check** comparing today's prices vs. hyperbitcoinization scenario
- **Investment perspective** on affordability of your Bitcoin requirement

## 📈 Key Insights

### Global vs US Wealth Inequality
- **Americans**: 6.9% of population, 30% of wealth (4.3x overrepresented)
- **Wealth Concentration**: Extreme inequality both globally and within the US

### Bitcoin Requirements by Wealth Level
| Net Worth | Global Percentile | US Percentile | Bitcoin Needed | Current Cost* |
|-----------|------------------|---------------|----------------|---------------|
| $25,000 | ~50% | ~25% | 0.00116714 | ~$79 |
| $100,000 | 82.2% | 46.8% | 0.00466857 | ~$315 |
| $500,000 | 95% | 85% | 0.02334286 | ~$1,576 |
| $1,000,000 | 98.5% | 90% | 0.04668571 | ~$3,153 |

*Based on ~$67,500 BTC price

### Standardized Percentiles
Both modes now use consistent percentiles for easy comparison:
**1%, 5%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 95%, 99%, 99.9%**

## 🔬 Methodology

### Data Processing
1. **UBS Wealth Pyramid**: Actual 2024 global wealth distribution
2. **Federal Reserve SCF**: US household wealth statistics  
3. **Proportional Allocation**: US gets 30% of Bitcoin supply matching 30% wealth share
4. **Linear Interpolation**: Between known percentile points
5. **Extended Precision**: Shows meaningful Bitcoin percentages
6. **Real-Time Integration**: Live Bitcoin pricing via API

### US vs Global Mode Differences

**Global Mode:**
- Compete globally for full 21M BTC supply
- Your wealth vs. $449.9T global wealth
- Shows global wealth percentile

**US Mode:**
- Compete only among Americans for 6.3M BTC allocation
- Your wealth vs. $135T US wealth  
- Shows US percentile + global context
- More realistic for American participants

### Limitations
- Assumes wealth distribution shape remains constant
- Doesn't account for Bitcoin lost/inaccessible (~20% estimated)
- Theoretical scenario for educational purposes
- Real hyperbitcoinization would have different dynamics
- API dependency for current pricing (fallback: $115,000)

## 📚 References

### Primary Sources
- **UBS Global Wealth Report 2024**: Official global wealth distribution
- **Federal Reserve SCF**: US household wealth statistics
- **CoinGecko API**: Real-time Bitcoin pricing
- **Bitcoin Protocol**: 21 million BTC hard cap

### Key Papers
- Davies, J., Lluberas, R., & Shorrocks, A. (2024). *Global Wealth Report 2024*. UBS.
- Federal Reserve. *Survey of Consumer Finances*. Various years.

## ⚖️ Disclaimer

This calculator is for educational and entertainment purposes only. It represents a theoretical thought experiment and should not be considered financial advice. Real-world hyperbitcoinization would involve complex economic dynamics not modeled here. Bitcoin investments carry significant risk.

*"Fix the money, fix the world."*
