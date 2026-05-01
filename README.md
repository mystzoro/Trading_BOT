# Binance Futures Testnet Trading Bot

A lightweight CLI-based trading bot for placing MARKET and LIMIT orders on Binance Futures testnet. 

## Features
- ✅ Place **MARKET** and **LIMIT** orders
- ✅ Support for **BUY** and **SELL** operations
- ✅ CLI-based input with validation
- ✅ Comprehensive logging to `bot.log`
- ✅ Error handling and API exception management
- ✅ Clean, modular project structure

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance API client initialization
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging setup
├── cli.py                     # CLI entry point
├── requirements.txt           # Dependencies
├── .env                       # API keys (do not commit)
├── .env.example               # Template for .env
├── .gitignore                 # Git ignore rules
├── bot.log                    # Execution logs
└── README.md                  # This file
```

## Setup

### 1. Create Binance Futures Testnet Account
- Go to [Binance Futures Testnet](https://testnet.binancefuture.com/)
- Create an account and generate API keys
- Enable futures trading permissions

### 2. Configure Environment
Create a `.env` file in the project root:
```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
BASE_URL=https://testnet.binancefuture.com
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### MARKET Order (Buy)
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order (Sell)
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000
```

### Expected Output
```
✅ ORDER SUCCESS
──────────────────────────────────────────────────
Order ID: 13095921164
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.001
Price: 75000.00
Avg Price: 0.00
Executed Qty: 0.0000
Status: NEW
──────────────────────────────────────────────────
```

## Logging
All orders and errors are logged to `bot.log` with timestamps and details:
- Request parameters (symbol, side, type, quantity, price)
- Full API response
- Error messages and stack traces

## Input Validation
The CLI validates:
- ✅ Required parameters (symbol, side, type, quantity)
- ✅ Valid side: `BUY` or `SELL`
- ✅ Valid order type: `MARKET` or `LIMIT`
- ✅ Positive quantity
- ✅ Price required for LIMIT orders

## Assumptions
- USDT-M (USDT Margined) futures only
- No leverage handling
- GTC (Good-Till-Cancel) time in force for LIMIT orders
- Binance testnet endpoint

## Testing
Both MARKET and LIMIT orders have been tested successfully:
- MARKET BUY order: ✅ Placed and logged
- LIMIT SELL order: ✅ Placed and logged

See `bot.log` for full execution logs.

## Notes
- Keep `.env` out of version control (added to `.gitignore`)
- Use `.env.example` as a template for sharing the project
- All API calls use the testnet endpoint by default
- Timestamps and logging are UTC+0
