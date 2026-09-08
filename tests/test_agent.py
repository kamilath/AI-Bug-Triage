from agent import process_bug


def test_payment_bug():

    result = process_bug(
        "Payment page crashes",
        "Application crashes when user makes a payment"
    )

    assert result["severity"] == "Critical"
    assert result["priority"] == "P0"
    assert result["component"] == "Payment"


def test_login_bug():

    result = process_bug(
        "Login failed",
        "User cannot login with valid credentials"
    )

    assert result["severity"] == "High"
    assert result["priority"] == "P1"
    assert result["component"] == "Authentication"


def test_test_cases():

    result = process_bug(
        "Search error",
        "Search returns incorrect results"
    )

    assert len(result["test_cases"]) > 0


def test_regression():

    result = process_bug(
        "Cart error",
        "Cart shows incorrect products"
    )

    assert len(result["regression_tests"]) > 0
