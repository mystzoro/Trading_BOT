import argparse

from trading_bot.bot.client import get_client
from trading_bot.bot.logging_config import setup_logger
from trading_bot.bot.orders import place_order
from trading_bot.bot.validators import validate_order


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Binance Futures testnet order CLI")
    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price")
    return parser


def main():
    logger = setup_logger()
    parser = build_parser()
    args = parser.parse_args()

    args.side = args.side.upper()
    args.type = args.type.upper()
    args.symbol = args.symbol.upper()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        print("\n✅ ORDER SUCCESS")
        print("─" * 50)
        print("Order ID:", order.get("orderId"))
        print("Symbol:", order.get("symbol"))
        print("Side:", order.get("side"))
        print("Type:", order.get("type"))
        print("Quantity:", order.get("origQty"))
        print("Price:", order.get("price"))
        print("Avg Price:", order.get("avgPrice"))
        print("Executed Qty:", order.get("executedQty"))
        print("Status:", order.get("status"))
        print("─" * 50)
        logger.info("Order completed successfully: %s", order.get("orderId"))
    except Exception as exc:
        logger.error("CLI error: %s", exc)
        print("\nERROR:", str(exc))


if __name__ == "__main__":
    main()
