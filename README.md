# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with Binance Futures Testnet to place MARKET and LIMIT orders with validation, logging, and modular architecture.

Built as part of a technical assessment to demonstrate API integration, CLI design, and structured Python development.

## Features
- Place **MARKET** and **LIMIT** orders
- Support for **BUY** and **SELL** operations
- CLI-based input with validation
- Logging to `bot.log`
- Error handling and API exception management
- Clean, modular project structure

## Architecture

`CLI -> Validation -> Order Execution -> Binance API -> Logging`

- `cli.py`: Handles user input and prints results
- `validators.py`: Validates symbols, order side, type, quantity, and price
- `orders.py`: Sends futures order requests to Binance
- `client.py`: Creates the Binance client using environment variables
- `logging_config.py`: Configures file and console logging

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
Quantity: 0.0010
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

## Error Handling

- Handles invalid CLI inputs before placing orders
- Catches Binance API exceptions during order submission
- Logs all failures in `bot.log` for debugging
- Prints concise error messages to the console

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

## Sample Output

```text
✅ ORDER SUCCESS
Order ID: 123456
Status: FILLED
Executed Qty: 0.0010
```

## Notes
- Keep `.env` out of version control (added to `.gitignore`)
- Use `.env.example` as a template for sharing the project
- All API calls use the testnet endpoint by default
- Timestamps and logging are UTC+0
