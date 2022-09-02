from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    '''Class to construct a custom pagination to limit the number of results despite the query parameter'''

    max_limit = 4
