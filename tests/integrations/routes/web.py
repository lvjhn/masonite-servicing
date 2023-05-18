from masonite.routes import Route

ROUTES = [
    Route.get("/add", "WelcomeController@add"),
    Route.get("/subtract", "WelcomeController@subtract"),
    Route.get("/multiply", "WelcomeController@multiply")
]
