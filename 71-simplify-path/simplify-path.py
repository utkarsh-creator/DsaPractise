class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        result = []
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if result:
                    result.pop()
            else:
                result.append(component)
        simplified_path = '/' + '/'.join(result)
        return simplified_path
