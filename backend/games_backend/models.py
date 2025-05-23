import enum
from typing import Any

import pydantic

# -------------------------------------
# Response Models
# -------------------------------------


class ResponseType(enum.Enum):
    SIMPLE = "simple"
    ERROR = "error"
    GAME_STATE = "game_state"
    SESSION_STATE = "session_state"


class ResponseParameters(pydantic.BaseModel):
    """
    A base class for all response parameters.
    """


class Response(pydantic.BaseModel):
    message_type: ResponseType
    # Implementations should implement there own parameters.


class SimpleResponseParameters(ResponseParameters):
    message: str


class SimpleResponse(Response):
    message_type: ResponseType = pydantic.Field(default=ResponseType.SIMPLE, init=False)
    parameters: SimpleResponseParameters


class ErrorResponseParameters(ResponseParameters):
    error_message: str


class ErrorResponse(Response):
    message_type: ResponseType = pydantic.Field(default=ResponseType.ERROR, init=False)
    parameters: ErrorResponseParameters


class GameStateResponseParameters(ResponseParameters):
    """
    A model representing game state parameters. This will be extended by each of the games.
    """


class GameStateResponse(Response):
    message_type: ResponseType = pydantic.Field(default=ResponseType.GAME_STATE, init=False)
    # Implementations should implement there own parameters.


class SessionStateResponseParameters(ResponseParameters):
    player_positions: dict[int, str | None]
    user_position: int | None


class SessionStateResponse(Response):
    message_type: ResponseType = pydantic.Field(default=ResponseType.SESSION_STATE, init=False)
    parameters: SessionStateResponseParameters


class GameParameters(pydantic.BaseModel):
    """
    Custom game specific information can be provided here.
    """


class GameType(enum.Enum):
    """
    When adding a new game type, try to make it match the path name in the frontend.
    """

    TICTACTOE = "tictactoe"
    ULTIMATE = "ultimate"


class GameMetadata(pydantic.BaseModel):
    game_type: GameType
    max_players: int
    parameters: GameParameters


# -------------------------------------
# Request Models
# -------------------------------------


class WebsocketRequestType(enum.Enum):
    SESSION = "session"
    GAME = "game"


class WebSocketRequest(pydantic.BaseModel):
    request_type: WebsocketRequestType
    function_name: str
    parameters: dict[str, Any]
