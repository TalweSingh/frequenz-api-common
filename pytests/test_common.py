# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.common package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import v1

    assert v1 is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import components_pb2

    assert components_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import components_pb2_grpc

    assert components_pb2_grpc is not None


def test_module_import_metrics() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import metrics_pb2

    assert metrics_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import metrics_pb2_grpc

    assert metrics_pb2_grpc is not None


def test_module_import_metrics_electrical() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import electrical_pb2

    assert electrical_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import electrical_pb2_grpc

    assert electrical_pb2_grpc is not None
