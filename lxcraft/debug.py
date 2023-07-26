import os


def debug(category: str, *args, **kwargs):
    debug_categories = os.environ.get("DEBUG", "").split(",")
    if [category, "all"] in debug_categories:
        print(f"DEBUG [{category}]: ", *args, **kwargs)
