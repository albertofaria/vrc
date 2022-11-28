import pytest
import typing

from vrc.loaders import ResolutionError


@pytest.fixture
def cython_loader() -> typing.Any:
    try:
        import vrc.loaders.cython_loader as cython_loader   # type: ignore
        return cython_loader
    except ModuleNotFoundError:
        pytest.skip('cython_loader not found')


def test_empty_args(cython_loader: typing.Any) -> None:
    with pytest.raises(ResolutionError):
        cython_loader.build_graph("test.c", [], "test.vrc", True)


def test_invalid_type_args(cython_loader: typing.Any) -> None:
    with pytest.raises(TypeError):
        cython_loader.build_graph("test.c", ["abc", 123, "def"], "test.vrc", True)


def test_none_filename(cython_loader: typing.Any) -> None:
    with pytest.raises(ResolutionError):
        cython_loader.build_graph(None, [], "test.vrc", True)


def test_invalid_type_filename(cython_loader: typing.Any) -> None:
    with pytest.raises(TypeError):
        cython_loader.build_graph(123, [], "test.vrc", True)


def test_none_out_path(cython_loader: typing.Any) -> None:
    with pytest.raises(TypeError):
        cython_loader.build_graph("test.c", [], None, True)


def test_invalid_type_out_path(cython_loader: typing.Any) -> None:
    with pytest.raises(TypeError):
        cython_loader.build_graph([], 123, True)


def test_dummy(cython_loader: typing.Any) -> None:
    with pytest.raises(ResolutionError):
        cython_loader.build_graph("nonexistent.c", ["nonexistent.c"], "test.vrc", True)
