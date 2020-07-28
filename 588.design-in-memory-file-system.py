class FileSystem:

    def __init__(self):
        self.root = dict()

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.root.keys())
        path_levels = path[1:].split('/')
        curr = self.root
        for level in path_levels:
            curr = curr[level]
        if isinstance(curr, str):
            return path
        elif isinstance(curr, dict):
            return sorted(curr.keys())

    def mkdir(self, path: str) -> None:
        dir_levels = path[1:].split('/')
        curr = self.root
        for level in dir_levels:
            curr[level] = curr.get(level, dict())
            curr = curr[level]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_levels = filePath[1:].split('/')
        dir_levels, file_name = path_levels[:-1], path_levels[-1]
        curr = self.root
        for level in dir_levels:
            curr = curr[level]
        curr[file_name] = curr.get(file_name, '') + content

    def readContentFromFile(self, filePath: str) -> str:
        path_levels = filePath[1:].split('/')
        curr = self.root
        for level in path_levels:
            curr = curr[level]
        return curr

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)