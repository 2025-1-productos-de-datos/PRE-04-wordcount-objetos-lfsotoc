

class TextProcessor:

    def preprocess_lines(self, lines):
        """
        Preprocess the lines of text by removing leading and trailing whitespace,
        converting to lowercase, and removing empty lines.
        """
        return [line.strip().lower().strip for line in lines if line.strip()]
