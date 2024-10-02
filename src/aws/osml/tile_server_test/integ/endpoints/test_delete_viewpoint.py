#  Copyright 2024 Amazon.com, Inc. or its affiliates.

from requests import Session


def delete_viewpoint(session: Session, url: str, viewpoint_id: str) -> None:
    """
    Test Case: Successfully delete the viewpoint

    :param session: Requests session to use to send the request.
    :param url: URL to send the request to.
    :param viewpoint_id: Unique viewpoint id to get from the table.

    return: None
    """
    res = session.delete(f"{url}/{viewpoint_id}")
    res.raise_for_status()

    assert res.status_code == 204


def delete_viewpoint_invalid(session: Session, url: str, viewpoint_id: str) -> None:
    """
    Test Case: Failed to delete the viewpoint

    :param session: Requests session to use to send the request.
    :param url: URL to send the request to.
    :param viewpoint_id: Unique viewpoint id to get from the table.

    return: None
    """
    res = session.delete(f"{url}/{viewpoint_id}")

    response_data = res.json()

    assert res.status_code == 404
    assert f"viewpoint_id {viewpoint_id} not found." in response_data["detail"]
