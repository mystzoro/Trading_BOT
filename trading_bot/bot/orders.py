import logging

logger = logging.getLogger("trading_bot")


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            "Placing order: symbol=%s side=%s type=%s quantity=%s price=%s",
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        order = client.futures_create_order(**order_params)
        logger.info("Order response: %s", order)
        return order
    except Exception as exc:
        logger.exception("Error placing order")
        raise RuntimeError(f"Error placing order: {exc}") from exc
