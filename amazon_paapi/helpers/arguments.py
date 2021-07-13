"""Module with helper functions for managing arguments."""


from ..tools import get_asin
from ..errors import InvalidArgumentException, AsinNotFoundException
from typing import List, Union


def get_items_ids(items: Union[str, List[str]]) -> List[str]:
    if not isinstance(items, str) and not isinstance(items, List):
        raise InvalidArgumentException('Invalid items argument, it should be a string or List of strings')

    if isinstance(items, str):
        items_ids = items.split(',')
        items_ids = [get_asin(x.strip()) for x in items_ids]

    else:
        items_ids = [get_asin(x.strip()) for x in items]

    if items_ids:
        return items_ids
    else:
        raise AsinNotFoundException('No ASIN codes have been found.')


def check_search_args(**kwargs):
    _check_search_mandatory_args(**kwargs)
    _check_search_pagination_args(**kwargs)


def _check_search_mandatory_args(**kwargs):
    mandatory_args = [kwargs['keywords'], kwargs['actor'], kwargs['artist'],
                      kwargs['author'],kwargs['brand'], kwargs['title']]
    if all(arg is None for arg in mandatory_args):
        error_message = ('At least one of the following args should be provided: '
                         'keywords, actor, artist, author, brand or title.')
        raise InvalidArgumentException(error_message)


def _check_search_pagination_args(**kwargs):
    pagination_args = [kwargs['item_count'], kwargs['item_page']]
    pagination_args = [arg for arg in pagination_args if arg]
    if not all(1 <= arg <= 10 and isinstance(arg, int) for arg in pagination_args):
        error_message = ('Args item_count and item_page should be integers between 1 and 10.')
        raise InvalidArgumentException(error_message)


def check_variations_args(**kwargs):
    pagination_args = [kwargs['variation_count'], kwargs['variation_page']]
    pagination_args = [arg for arg in pagination_args if arg]
    if not all(1 <= arg <= 10 and isinstance(arg, int) for arg in pagination_args):
        error_message = ('Args variation_count and variation_page should be integers between 1 and 10.')
        raise InvalidArgumentException(error_message)


def check_browse_nodes_args(**kwargs):
    if not isinstance(kwargs['browse_node_ids'], List):
        error_message = 'Argument browse_node_ids should be a List of strings.'
        raise InvalidArgumentException(error_message)