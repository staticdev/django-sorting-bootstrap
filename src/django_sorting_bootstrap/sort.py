"""Sort module."""


def sort_queryset(queryset, request, context=None):
    """Return a sorted queryset."""
    sort_by = request.GET.get("sort_by")
    if sort_by:
        if sort_by in [el.name for el in queryset.model._meta.fields]:
            queryset = queryset.order_by(sort_by)
        else:
            if sort_by in request.session:
                sort_by = request.session[sort_by]
                try:
                    queryset = queryset.order_by(sort_by)
                except Exception:
                    raise
            # added else to fix a bug when using changelist
            # TODO: use less ifs and more standard sorting
            elif context is not None:
                # sorted ascending
                if sort_by[0] != "-":
                    sort_by = context["cl"].list_display[int(sort_by) - 1]
                # sorted descending
                else:
                    sort_by = "-" + context["cl"].list_display[abs(int(sort_by)) - 1]
                queryset = queryset.order_by(sort_by)
    return queryset
