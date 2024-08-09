#  Copyright 2024 Amazon.com, Inc. or its affiliates.

from argparse import ArgumentParser

from src.aws.osml.tile_sever_test.integ_processor import TSIntegTestProcessor

if __name__ == "__main__":
    """
    Entry point for the tile server integration test processor.

    This script is used to run integration tests for a tile server using the
    specified container image URI.

    The script accepts the following command-line arguments:

    - ``--image_uri``: The URI of the container image to test with.

    Example usage:

    .. code-block:: console

        python ts_integ_test.py --image_uri <image_uri>

    The ``image_uri`` is passed to the `TSIntegTestProcessor` for further processing.
    """
    parser = ArgumentParser("ts_integ_test")
    parser.add_argument("--image_uri", help="The image to test with.", type=str)
    TSIntegTestProcessor(vars(parser.parse_args()))
