from starlette.routing import Route, Mount
from example_services.apis.service import Root
from example_services.apis.example import (
    ExampleListCreateAPIView,
    ExampleRetrieveUpdateDestroyAPIView,
)

# Add your routes here
routes = [
    Route("/", Root.api_name, methods=["GET"]),
    Route("/api/version", Root.api_version, methods=["GET"]),
    Mount(
        "/api/v1/examples",
        routes=[
            Route("/", ExampleListCreateAPIView, methods=["GET", "POST"]),
            Route(
                "/{uuid}",
                ExampleRetrieveUpdateDestroyAPIView,
                methods=["GET", "PATCH", "DELETE"],
            ),
        ],
    ),
]
