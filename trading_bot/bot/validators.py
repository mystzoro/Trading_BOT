def validate_order(symbol, side, order_type, quantity, price=None):
    if not symbol or not symbol.strip():
        raise ValueError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        if price <= 0:
            raise ValueError("Price must be positive")
