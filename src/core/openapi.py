# src/core/openapi.py
from typing import Any, Dict

from users.user_schemas import User, UserInput


def get_openapi_spec() -> Dict[str, Any]:
    """Retorna o dicionário com a especificação OpenAPI 3.0.3 da aplicação."""
    user_schema = User.model_json_schema()
    user_input_schema = UserInput.model_json_schema()

    return {
        "openapi": "3.0.3",
        "info": {
            "title": "template-servico-python",
            "version": "1.0.0",
            "description": "API REST do template de serviço Python",
        },
        "paths": {
            "/": {
                "get": {
                    "summary": "Root endpoint",
                    "description": "Returns welcome message.",
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {"text/html": {"schema": {"type": "string"}}},
                        }
                    },
                }
            },
            "/health": {
                "get": {
                    "summary": "Health Check",
                    "description": (
                        "Validates application status and database connectivity."
                    ),
                    "responses": {
                        "200": {
                            "description": "Application and database are healthy",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "status": {
                                                "type": "string",
                                                "example": "ok",
                                            },
                                            "database": {
                                                "type": "string",
                                                "example": "connected",
                                            },
                                        },
                                        "required": ["status", "database"],
                                    }
                                }
                            },
                        },
                        "503": {
                            "description": (
                                "Database connection failure or service unhealthy"
                            ),
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "status": {
                                                "type": "string",
                                                "example": "unhealthy",
                                            },
                                            "database": {
                                                "type": "string",
                                                "example": "disconnected",
                                            },
                                        },
                                        "required": ["status", "database"],
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/users/": {
                "get": {
                    "summary": "List users",
                    "description": "Retrieves all users from the database.",
                    "responses": {
                        "200": {
                            "description": "List of registered users",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/User"},
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create user",
                    "description": "Creates a new user with input validation.",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/UserInput"}
                            }
                        },
                    },
                    "responses": {
                        "201": {
                            "description": "User successfully created",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        },
                        "400": {
                            "description": "Validation error or invalid payload",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {"error": {"type": "string"}},
                                    }
                                }
                            },
                        },
                    },
                },
            },
            "/users/{user_id}": {
                "get": {
                    "summary": "Get user by ID",
                    "description": "Retrieves a specific user by unique identifier.",
                    "parameters": [
                        {
                            "name": "user_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"},
                            "description": "Unique identifier of the user",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "User found",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        },
                        "404": {
                            "description": "User not found",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "error": {
                                                "type": "string",
                                                "example": "User not found",
                                            }
                                        },
                                    }
                                }
                            },
                        },
                    },
                }
            },
        },
        "components": {
            "schemas": {
                "User": user_schema,
                "UserInput": user_input_schema,
            }
        },
    }
