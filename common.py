import os


def check_file_can_access_on_windows(file_path):
    result = False
    if os.path.exists(file_path):
        try:
            os.rename(file_path, file_path)
            result = True
        except OSError:
            result = False
    return result
