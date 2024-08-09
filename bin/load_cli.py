#  Copyright 2024 Amazon.com, Inc. or its affiliates.

from argparse import ArgumentParser
from distutils.util import strtobool

from src.aws.osml.tile_sever_test.load_processor import TSLoadTestProcessor


def list_of_strings(arg) -> list:
    """
    Convert a comma-separated string into a list of strings.

    :param arg: A comma-separated string.
    :return: A list of strings.
    """
    return arg.split(",")


if __name__ == "__main__":
    """
    Entry point for the tile server load test processor.

    This script is used to run load tests for a tile server using the specified
    configuration options.

    The script accepts the following command-line arguments:

    - ``--image_uri``: The URI of the container image to test with.
    - ``--source_image_bucket``: The S3 bucket containing images to use for Tile Server tests.
    - ``--locust_headless``: Disable the Locust web interface and start the test immediately (default: False).
    - ``--locust_users``: Peak number of concurrent Locust users (default: "1").
    - ``--locust_run_time``: Duration to run the load test, e.g., 300s, 20m, 3h, etc. (default: "5m").
    - ``--locust_spawn_rate``: Rate to spawn users at (users per second) (default: "1").
    - ``--locust_image_keys``: Comma-separated list of image keys to use for the load test.

    Example usage:

    .. code-block:: console

        python ts_load_test.py --image_uri <image_uri> --source_image_bucket <bucket_name>
            --locust_users 10 --locust_run_time 10m

    The arguments are passed to the `TSLoadTestProcessor` for further processing.
    """
    parser = ArgumentParser("ts_load_test")
    parser.add_argument("--image_uri", help="Endpoint of the Tile Server to test", type=str)
    parser.add_argument("--source_image_bucket", help="Bucket containing images to use for Tile Server tests.", type=str)
    parser.add_argument(
        "--locust_headless",
        help="Load Test: Disable the web interface, and start the test immediately.",
        type=lambda x: bool(strtobool(str(x))),
        default=False,
    )
    parser.add_argument("--locust_users", help="Load Test: Peak number of concurrent Locust users.", type=str, default="1")
    parser.add_argument(
        "--locust_run_time",
        help="Load Test: Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.)",
        type=str,
        default="5m",
    )
    parser.add_argument(
        "--locust_spawn_rate", help="Load Test: Rate to spawn users at (users per second).", type=str, default="1"
    )
    parser.add_argument(
        "--locust_image_keys",
        help="Load Test: Comma separated list of image keys to use for the load test.",
        type=list_of_strings,
        default=[],
    )
    TSLoadTestProcessor(vars(parser.parse_args()))
