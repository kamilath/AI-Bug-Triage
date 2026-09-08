def generate_test_cases(title, description, component):
    
    if component == "Payment":
        return [
            {
                "id": "TC001",
                "title": "Verify payment with valid card",
                "steps": [
                    "Open payment page",
                    "Enter valid card details",
                    "Click Pay"
                ],
                "expected": "Payment should be completed successfully"
            },
            {
                "id": "TC002",
                "title": "Verify payment with expired card",
                "steps": [
                    "Open payment page",
                    "Enter expired card details",
                    "Click Pay"
                ],
                "expected": "Payment should be rejected with proper error message"
            },
            {
                "id": "TC003",
                "title": "Verify payment with invalid card",
                "steps": [
                    "Open payment page",
                    "Enter invalid card details",
                    "Click Pay"
                ],
                "expected": "Proper validation message should be displayed"
            },
            {
                "id": "TC004",
                "title": "Verify payment cancellation",
                "steps": [
                    "Open payment page",
                    "Enter valid payment details",
                    "Cancel payment"
                ],
                "expected": "Payment should be cancelled successfully"
            }
        ]

    elif component == "Authentication":
        return [
            {
                "id": "TC001",
                "title": "Verify login with valid credentials",
                "steps": [
                    "Open login page",
                    "Enter valid username",
                    "Enter valid password",
                    "Click Login"
                ],
                "expected": "User should login successfully"
            },
            {
                "id": "TC002",
                "title": "Verify login with invalid credentials",
                "steps": [
                    "Open login page",
                    "Enter invalid username",
                    "Enter invalid password",
                    "Click Login"
                ],
                "expected": "Proper login error should be displayed"
            },
            {
                "id": "TC003",
                "title": "Verify login with empty credentials",
                "steps": [
                    "Open login page",
                    "Leave username empty",
                    "Leave password empty",
                    "Click Login"
                ],
                "expected": "Required field validation should be displayed"
            }
        ]

    elif component == "Shopping Cart":
        return [
            {
                "id": "TC001",
                "title": "Verify adding product to cart",
                "steps": [
                    "Open product page",
                    "Select a product",
                    "Click Add to Cart"
                ],
                "expected": "Product should be added to cart"
            },
            {
                "id": "TC002",
                "title": "Verify removing product from cart",
                "steps": [
                    "Open cart",
                    "Select a product",
                    "Click Remove"
                ],
                "expected": "Product should be removed from cart"
            },
            {
                "id": "TC003",
                "title": "Verify cart total calculation",
                "steps": [
                    "Add multiple products",
                    "Open cart",
                    "Check total"
                ],
                "expected": "Cart total should be calculated correctly"
            }
        ]

    elif component == "Search":
        return [
            {
                "id": "TC001",
                "title": "Verify search with valid product",
                "steps": [
                    "Open search",
                    "Enter valid product",
                    "Click Search"
                ],
                "expected": "Relevant products should be displayed"
            },
            {
                "id": "TC002",
                "title": "Verify search with invalid product",
                "steps": [
                    "Open search",
                    "Enter unavailable product",
                    "Click Search"
                ],
                "expected": "No results message should be displayed"
            },
            {
                "id": "TC003",
                "title": "Verify search with empty input",
                "steps": [
                    "Open search",
                    "Leave search field empty",
                    "Click Search"
                ],
                "expected": "Proper validation should be displayed"
            }
        ]

    else:
        return [
            {
                "id": "TC001",
                "title": f"Verify {component} with valid data",
                "steps": [
                    "Open application",
                    f"Navigate to {component}",
                    "Enter valid data",
                    "Perform the reported action"
                ],
                "expected": "Functionality should work successfully"
            },
            {
                "id": "TC002",
                "title": f"Verify {component} with invalid data",
                "steps": [
                    "Open application",
                    f"Navigate to {component}",
                    "Enter invalid data",
                    "Perform the reported action"
                ],
                "expected": "Proper error message should be displayed"
            }
        ]


def generate_regression(component):

    if component == "Payment":
        return [
            "Verify payment with valid card",
            "Verify payment with invalid card",
            "Verify payment with expired card",
            "Verify payment cancellation",
            "Verify payment failure handling",
            "Verify order creation after successful payment"
        ]

    elif component == "Authentication":
        return [
            "Verify login with valid credentials",
            "Verify login with invalid credentials",
            "Verify empty username",
            "Verify empty password",
            "Verify logout",
            "Verify password reset"
        ]

    elif component == "Shopping Cart":
        return [
            "Verify adding product to cart",
            "Verify removing product from cart",
            "Verify updating product quantity",
            "Verify cart total calculation",
            "Verify checkout from cart"
        ]

    elif component == "Search":
        return [
            "Verify valid product search",
            "Verify invalid product search",
            "Verify empty search",
            "Verify search result accuracy",
            "Verify search result sorting"
        ]

    else:
        return [
            f"Verify {component} with valid data",
            f"Verify {component} with invalid data",
            f"Verify {component} error handling",
            f"Verify {component} after application restart"
        ]