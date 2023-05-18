from masonite.routes import Route

ROUTES = [
    # CALCULATOR DEMO # 
    Route.group(
        [
            Route.get("/add", "CalculatorController@add"),
            Route.get("/subtract", "CalculatorController@subtract"),
            Route.get("/multiply", "CalculatorController@multiply"), 
            Route.get("/divide", "CalculatorController@divide")
        ],
        prefix="/calculator"
    )
]
