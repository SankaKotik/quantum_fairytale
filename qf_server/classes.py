import os

class FolderFiles:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = {}

    def read_files(self):
        for file_name in os.listdir(self.folder_path):
            with open(os.path.join(self.folder_path, file_name), 'r') as f:
                content = f.read()
                file_title = os.path.splitext(file_name)[0]
                self.files[file_title] = content

    def __getattr__(self, name):
        if name in self.files:
            return self.files[name]
        else:
            return None

