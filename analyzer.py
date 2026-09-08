def analyze_bug(title, description):
    text = (title + " " + description).lower()

    if any(word in text for word in ["crash", "payment", "data loss", "security"]):
        severity = "Critical"
    elif any(word in text for word in ["cannot login", "login failed", "checkout", "error"]):
        severity = "High"
    elif any(word in text for word in ["slow", "incorrect", "wrong"]):
        severity = "Medium"
    else:
        severity = "Low"

    if severity == "Critical":
        priority = "P0"
    elif severity == "High":
        priority = "P1"
    elif severity == "Medium":
        priority = "P2"
    else:
        priority = "P3"

    if any(word in text for word in ["login", "password", "authentication"]):
        component = "Authentication"
    elif any(word in text for word in ["payment", "card", "transaction"]):
        component = "Payment"
    elif any(word in text for word in ["cart", "product"]):
        component = "Shopping Cart"
    elif any(word in text for word in ["search"]):
        component = "Search"
    else:
        component = "Other"

    return {
        "severity": severity,
        "priority": priority,
        "component": component
    }