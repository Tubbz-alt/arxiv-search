from .base import Property, DateRange, Query, ClassificationList


class FieldedSearchTerm(dict):
    """Represents a fielded search term."""

    operator = Property('operator', str)
    field = Property('field', str)
    term = Property('term', str)

    def __str__(self):
        """Build a string representation, for use in rendering."""
        return f'{self.operator} {self.field}={self.term}'


class FieldedSearchList(list):
    def __str__(self):
        """Build a string representation, for use in rendering."""
        return '; '.join([str(item) for item in self])


class AdvancedQuery(Query):
    date_range = Property('date_range', DateRange)
    primary_classification = Property('primary_classification',
                                      ClassificationList)
    terms = Property('terms', FieldedSearchList, FieldedSearchList())