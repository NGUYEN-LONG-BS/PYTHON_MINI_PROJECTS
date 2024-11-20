def get_id(link):
    source_id = link[link.rfind('-') + 1:link.find('.html')]
    source_id = int(source_id.replace("a", "").replace("b", ""))

    return source_id