#!/usr/bin/env python3
"""
Bitcoin World Wealth Percentile Calculator

Calculate how much Bitcoin you would need to maintain your current wealth 
percentile if Bitcoin became the world's only store of value.

Data Sources:
- Global: UBS Global Wealth Report 2024 (actual data)
- US: Federal Reserve Survey of Consumer Finances
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict

class BitcoinWealthCalculator:
    def __init__(self):
        # Global wealth from UBS Global Wealth Report 2024
        self.global_wealth = 449.9e12  # $449.9 trillion
        self.bitcoin_supply = 21e6     # 21 million BTC
        self.btc_price = self.global_wealth / self.bitcoin_supply
        
        # Global wealth distribution (UBS 2024 - actual data)
        # Based on wealth pyramid: 3.767B adults, $449.9T total
        self.global_percentiles = {
            0: -5000,       # Bottom
            10: 1500,       # Within <$10k band
            20: 3500,
            30: 6000,
            39.5: 10000,    # UBS boundary: bottom 39.5%
            50: 25000,      # Estimated median
            60: 40000,
            70: 60000,
            80: 85000,
            82.2: 100000,   # UBS boundary: bottom 82.2%
            90: 200000,
            95: 500000,
            98.5: 1000000,  # UBS boundary: top 1.5%
            99: 1500000,
            99.5: 5000000,
            99.9: 25000000,
            100: 100000000
        }
        
        # US wealth distribution (Federal Reserve SCF)
        self.us_percentiles = {
            0: -10000,
            10: 0,
            25: 15000,
            50: 121000,     # US median
            75: 403000,
            90: 1200000,
            95: 2400000,
            99: 11100000,
            99.5: 21000000,
            99.9: 43200000,
            100: 500000000
        }
        
        # Current mode
        self.use_global = True
    
    def get_percentiles(self):
        """Get current percentile dictionary"""
        return self.global_percentiles if self.use_global else self.us_percentiles
    
    def get_percentile_from_wealth(self, wealth: float) -> float:
        """Calculate percentile from net worth using interpolation"""
        percentiles = self.get_percentiles()
        pcts = list(percentiles.keys())
        values = list(percentiles.values())
        
        if wealth <= values[0]:
            return pcts[0]
        if wealth >= values[-1]:
            return pcts[-1]
        
        # Linear interpolation
        for i in range(len(values) - 1):
            if values[i] <= wealth <= values[i + 1]:
                ratio = (wealth - values[i]) / (values[i + 1] - values[i])
                return pcts[i] + ratio * (pcts[i + 1] - pcts[i])
        
        return 50.0
    
    def get_wealth_from_percentile(self, percentile: float) -> float:
        """Calculate net worth from percentile using interpolation"""
        percentiles = self.get_percentiles()
        pcts = list(percentiles.keys())
        values = list(percentiles.values())
        
        if percentile <= pcts[0]:
            return values[0]
        if percentile >= pcts[-1]:
            return values[-1]
        
        # Linear interpolation
        for i in range(len(pcts) - 1):
            if pcts[i] <= percentile <= pcts[i + 1]:
                ratio = (percentile - pcts[i]) / (pcts[i + 1] - pcts[i])
                return values[i] + ratio * (values[i + 1] - values[i])
        
        return percentiles[50]
    
    def calculate_bitcoin_needed(self, net_worth: float) -> Dict:
        """Calculate Bitcoin needed to maintain wealth percentile"""
        current_percentile = self.get_percentile_from_wealth(net_worth)
        
        # Direct conversion: wealth / BTC price
        bitcoin_needed = net_worth / self.btc_price
        
        # Calculate percentages
        wealth_fraction = (net_worth / self.global_wealth) * 100
        supply_percentage = (bitcoin_needed / self.bitcoin_supply) * 100
        
        return {
            'net_worth': net_worth,
            'percentile': current_percentile,
            'bitcoin_needed': bitcoin_needed,
            'wealth_fraction': wealth_fraction,
            'supply_percentage': supply_percentage,
            'data_source': 'Global (UBS 2024)' if self.use_global else 'US (Fed SCF)'
        }
    
    def format_percentage(self, pct: float) -> str:
        """Format percentage with appropriate decimal places"""
        if pct >= 1:
            return f"{pct:.3f}%"
        elif pct >= 0.1:
            return f"{pct:.4f}%"
        elif pct >= 0.01:
            return f"{pct:.5f}%"
        elif pct >= 0.001:
            return f"{pct:.6f}%"
        elif pct >= 0.0001:
            return f"{pct:.7f}%"
        else:
            return f"{pct:.8f}%"
    
    def generate_table(self) -> pd.DataFrame:
        """Generate percentile table"""
        if self.use_global:
            percentiles = [1, 5, 10, 25, 39.5, 50, 75, 82.2, 90, 95, 98.5, 99, 99.5, 99.9]
            source = "Global"
        else:
            percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99, 99.5, 99.9]
            source = "US"
        
        results = []
        for pct in percentiles:
            wealth = self.get_wealth_from_percentile(pct)
            calc = self.calculate_bitcoin_needed(wealth)
            
            results.append({
                f'{source} Percentile': f"{pct}%",
                'Net Worth Threshold': f"${wealth:,.0f}",
                'Bitcoin Needed': f"{calc['bitcoin_needed']:.8f}",
                '% of Bitcoin Supply': self.format_percentage(calc['supply_percentage'])
            })
        
        return pd.DataFrame(results)
    
    def plot_distribution(self):
        """Create visualization of Bitcoin distribution"""
        percentiles = np.linspace(1, 99.9, 50)
        bitcoin_amounts = []
        
        for p in percentiles:
            wealth = self.get_wealth_from_percentile(p)
            result = self.calculate_bitcoin_needed(wealth)
            bitcoin_amounts.append(result['bitcoin_needed'])
        
        plt.figure(figsize=(12, 8))
        
        # Main plot
        plt.subplot(2, 1, 1)
        plt.semilogy(percentiles, bitcoin_amounts)
        source = "Global" if self.use_global else "US"
        plt.xlabel(f'{source} Wealth Percentile (%)')
        plt.ylabel('Bitcoin Needed (BTC)')
        plt.title(f'Bitcoin Needed to Maintain {source} Wealth Percentile')
        plt.grid(True, alpha=0.3)
        
        # Zoomed view
        plt.subplot(2, 1, 2)
        mask = np.array(bitcoin_amounts) <= 1
        plt.plot(np.array(percentiles)[mask], np.array(bitcoin_amounts)[mask])
        plt.xlabel(f'{source} Wealth Percentile (%)')
        plt.ylabel('Bitcoin Needed (BTC)')
        plt.title('Bitcoin Needed - Zoomed View (≤1 BTC)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def switch_to_global(self):
        """Switch to global wealth data"""
        self.use_global = True
        print("\n✓ Switched to GLOBAL wealth distribution (UBS 2024)")
        print("Data: UBS Global Wealth Report 2024")
        print("Sample: 3.767 billion adults, $449.9 trillion")
        print("Key thresholds: Top 1.5%: $1M+ | Top 17.8%: $100K+ | Median: ~$25K\n")
    
    def switch_to_us(self):
        """Switch to US wealth data"""
        self.use_global = False
        print("\n✓ Switched to US wealth distribution (Federal Reserve)")
        print("Data: Survey of Consumer Finances")
        print("Key thresholds: Top 1%: $11.1M+ | Top 10%: $1.2M+ | Median: $121K\n")
    
    def print_header(self):
        """Print calculator header"""
        print("=== Bitcoin World Wealth Percentile Calculator ===\n")
        print(f"Global Wealth: ${self.global_wealth/1e12:.1f} trillion")
        print(f"Bitcoin Supply: {self.bitcoin_supply/1e6:.0f} million BTC")
        print(f"BTC Price (hyperbitcoinization): ${self.btc_price:,.0f}")
        print("\nCommands:")
        print("  [number] - Calculate Bitcoin needed for net worth")
        print("  'global' - Switch to global data")
        print("  'us'     - Switch to US data")
        print("  'table'  - Show percentile table")
        print("  'plot'   - Show visualization")
        print("  'quit'   - Exit\n")

def main():
    calculator = BitcoinWealthCalculator()
    calculator.print_header()
    
    while True:
        try:
            user_input = input("Input: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            elif user_input.lower() == 'global':
                calculator.switch_to_global()
            
            elif user_input.lower() == 'us':
                calculator.switch_to_us()
            
            elif user_input.lower() == 'table':
                source = "Global" if calculator.use_global else "US"
                print(f"\n=== Bitcoin Needed by {source} Percentile ===")
                table = calculator.generate_table()
                print(table.to_string(index=False))
                print()
            
            elif user_input.lower() == 'plot':
                calculator.plot_distribution()
            
            else:
                # Parse net worth
                net_worth = float(user_input.replace('$', '').replace(',', ''))
                result = calculator.calculate_bitcoin_needed(net_worth)
                
                source = "Global" if calculator.use_global else "US"
                print(f"\n=== Results for ${net_worth:,.0f} ({result['data_source']}) ===")
                print(f"{source} percentile: {result['percentile']:.2f}%")
                print(f"Bitcoin needed: {result['bitcoin_needed']:.8f} BTC")
                print(f"% of Bitcoin supply: {calculator.format_percentage(result['supply_percentage'])}")
                print(f"% of global wealth: {result['wealth_fraction']:.8f}%\n")
        
        except ValueError:
            print("Please enter a valid number or command.\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()