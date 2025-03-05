# ruff: noqa: D103 - undocumented-public-function
import pytest

from src.commands import CommandError, InvalidCommandError
from src.game import create_game


def test_command_error():
    command_error = CommandError("test")

    assert command_error.message == "test"

    with pytest.raises(CommandError, match="test"):
        raise command_error


def test_invalid_command_error():
    invalid_command_error = InvalidCommandError("test")

    assert invalid_command_error.message == "Invalid command: test"

    with pytest.raises(InvalidCommandError, match="test"):
        raise invalid_command_error


def test_handle():
    game = create_game()
    commands = game.commands

    with pytest.raises(InvalidCommandError, match="test"):
        commands.handle("test", [])

    assert commands.handle("end", []) is None
    assert not game.current_player.is_starting_player()


def test_end():
    game = create_game()
    commands = game.commands

    assert commands.handle("end", []) is None
    assert not game.current_player.is_starting_player()
