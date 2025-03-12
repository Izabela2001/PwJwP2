from json import load

class MobileApp:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    download_count = 0

    @staticmethod
    def new_download():
        MobileApp.download_count += 1

    @classmethod
    def total_downloads(cls):
        return cls.download_count

    @classmethod
    def import_data_from_json(cls, path):
        with open(path, 'r') as f:
            data = load(f)
        return cls(data['name'], data['version'])