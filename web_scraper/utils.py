class Utils:
    @staticmethod
    def summarize_structure(tags):
        structure = {}
        for tag in tags:
            if tag.name not in structure:
                structure[tag.name] = 0
            structure[tag.name] += 1
        return structure