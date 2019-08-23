import re


def get_pagination_page_array(page, total_pages):
    """
    Return an array of page numbers to display for a given page with
    an offset around it.
    E.g with the current page page=4 and offset 2:
        [2,3,4,5,6]
    The total amount of pages is needed for boundary calculation.
    """
    first_page_to_show = page - 4
    last_page_to_show = page + 4

    first_page_offset = 0

    if first_page_to_show < 1:
        first_page_offset = first_page_to_show * -1 + 1
        first_page_to_show = 1

    if last_page_to_show > total_pages:
        if first_page_to_show > 1 and first_page_offset == 0:
            first_page_to_show = max(
                first_page_to_show - last_page_to_show + total_pages, 1
            )
        last_page_to_show = total_pages
    else:
        last_page_to_show = min(
            total_pages, last_page_to_show + first_page_offset
        )

    return list(range(first_page_to_show, last_page_to_show + 1))


def get_download_url(platform_category):
    """Return a download url for the matching platform"""
    if re.search(r"desktop|laptop", platform_category, re.IGNORECASE):
        return "https://ubuntu.com/download/desktop"
    if re.search(r"server", platform_category, re.IGNORECASE):
        return "https://ubuntu.com/download/server/"
    if re.search(r"core", platform_category, re.IGNORECASE):
        return "https://ubuntu.com/download/iot/"
    return "https://ubuntu.com/download"
