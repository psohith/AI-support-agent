from urllib.parse import urljoin

def filter_links(links, base_url):
    """
    Filter links that start with:
    1. `https://testsigma.com/docs/`
    2. `/docs/...` (relative links),
    while skipping links that contain `#`.
    """
    valid_links = []
    for link in links:
        if "#" in link:
            # Skip links containing `#`
            continue
        if link.startswith("https://testsigma.com/docs/"):
            valid_links.append(link)
        elif link.startswith("/docs"):
            # Convert relative URL to absolute
            full_link = urljoin(base_url, link)
            valid_links.append(full_link)
    return valid_links
