
# KOI - Portfolio Analysis Tool

![KOI Logo](image\benchmark_portfolio.png)

## Overview

KOI is a versatile and comprehensive tool for analyzing and benchmarking investment portfolios, with a specific focus on climate tech and thematic sectors. KOI leverages Yahoo Finance data to support all major stock exchanges and currencies, enabling global portfolio management. With KOI, you can evaluate individual stocks, analyze custom portfolios, and benchmark various thematic sectors, all while selecting your preferred currency reference.

## Key Features

- **Global Market Access**: KOI supports all stock exchanges and currencies provided by Yahoo Finance, making it a truly global portfolio management tool.
- **Flexible Currency Reference**: Choose between USD or EUR as the reference currency for all analysis and reporting.
- **Diverse Weighting Methodologies**: Apply different weighting methods to your portfolio, including equal weighting (`iso`), custom weights, and random weights for experimentation and analysis.
- **Comprehensive Return Calculations**: KOI calculates both capital gains and dividends, providing an accurate total return.
- **Benchmark portfolio performance**: KOI automatically benchmarks your portfolio performance against the most famous index
- **Annualized Return Calculation**: Calculate annualized gains based on the time of purchase for a precise measure of performance.
- **Risk-Adjusted Return Analysis**: Measure portfolio risk-adjusted returns using the US Treasury yield as the risk-free rate.
- **Sharpe Ratio Calculation**: Evaluate the Sharpe Ratio of your portfolio, a key metric that measures risk-adjusted return.
- **Relative Strength Index (RSI) Calculation**: Helps investors assess the timing of their investments by calculating the RSI, a popular momentum indicator used to evaluate overbought or oversold conditions.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/KOI.git
   cd KOI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   > **Note**: KOI requires an internet connection to fetch stock data through the `yfinance` library.

## Setup

Before starting your analysis, ensure you have a stable internet connection for Yahoo Finance data access. You may also need to set up a configuration file for custom portfolios (see [Configuration](#configuration)).

## Usage

### 1. Running KOI

The main entry point is `main.py`. Run the following command to start the program:
```bash
python main.py
```

### 2. Choosing a Stock

Upon running the tool, you will be prompted to enter the ticker symbol of the stock you wish to analyze (e.g., `TSLA` for Tesla). KOI will validate the ticker against Yahoo Finance.

### 3. Selecting Analysis Duration

You’ll also need to specify the analysis period by entering the number of years (e.g., 5 for a 5-year historical analysis). KOI will calculate the start and end dates based on the provided duration.

### 4. Portfolio Analysis and Benchmarking

KOI includes several pre-configured thematic portfolios, such as:
- **ClimateTech**: Covering solar, wind, storage, and other climate tech sectors.
- **Artificial Intelligence and Automation**
- **Healthcare**
- **Fossil Fuels**: Including Coal and Oil & Gas sectors.

To analyze or benchmark specific portfolios, go to `main.py` and uncomment the corresponding functions. You can customize portfolio allocations by editing the predefined lists in `portfolio_analyzer.py` or loading from an external configuration file.

## Configuration

KOI includes several thematic portfolios that you can configure by editing the relevant files. For more flexibility, you can also load portfolio configurations from a JSON or CSV file.

**Example Portfolio Configuration (JSON format):**
```json
{
  "ClimateTech_SOLAR": ["AGX", "NXT", "ENPH"],
  "ClimateTech_WIND": ["TPIC", "VWSB.DE", "GE"]
}
```

Save this file as `portfolios.json` and update `main.py` to load custom portfolios dynamically.

## Important Features and Options

- **Stock and Currency Support**: Supports all stocks and currencies available on Yahoo Finance.
- **Currency Reference**: Specify USD or EUR as the reference currency for analysis.
- **Weighting Methodologies**: Choose between equal weighting (`iso`), custom weights, or random weights to explore different portfolio compositions.
- **Return Calculation**: KOI includes both capital gains and dividends in return calculations, providing a comprehensive total return measure.
- **Annualized Return**: Calculates the annualized return based on the date of purchase, offering a standardized performance measure.
- **Risk-Adjusted Return**: Calculates risk-adjusted returns for your portfolio using the US Treasury yield as the risk-free rate, providing insights into performance relative to risk.
- **Sharpe Ratio**: Provides the Sharpe Ratio, helping investors assess the risk-adjusted performance of their portfolio.
- **Investment Timing with RSI**: Calculates the Relative Strength Index (RSI), allowing investors to assess if a stock is overbought or oversold, which can assist in timing investment decisions.

## Examples

### Example 1: Single Stock Analysis

```plaintext
Enter stock ticker: TSLA
Enter duration (years): 5
```

This will analyze Tesla’s performance over the past 5 years, displaying key metrics, performance charts, and RSI values.

### Example 2: ClimateTech Portfolio Benchmarking

To benchmark the ClimateTech portfolio, ensure that relevant sections in `main.py` are uncommented. This will display charts comparing the performance of solar, wind, and storage portfolios.

## Screenshots

Here are some sample outputs:

### Total Returns Plot
![Total Returns](path_to_example_chart.png)

### Portfolio Pie Chart
![Portfolio Distribution](path_to_pie_chart.png)

## License

