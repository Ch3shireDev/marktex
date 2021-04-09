
def split_filename(filename):
    parts = filename.split('.')
    base = '.'.join(parts[:-1])
    ext = parts[-1]
    return base, ext
