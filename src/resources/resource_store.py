import re


class ResourceStore:
    def __init__(self, resources: dict):
        self.resources = resources

    @staticmethod
    def is_valid_dot_notation(given_string: str):
        """
        Returns True if the given string is valid dot notation.
        """

        dot_notation_regex = r"^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*$"
        return re.match(dot_notation_regex, given_string) is not None

    def get_attribute(self, path: str):
        """
        Return the attribute at the given path. The path is
        the string of the dot notation.

        path: str - dot notation like so: "HelloWorldFunction.Properties.Handler"

        Must return a string, will raise an exception if
        anything else is attempted to be returned.
        """

        if not path:
            raise Exception("No attribute path given.")

        if not self.is_valid_dot_notation(path):
            raise Exception("Invalid dot notation.")

        keys = path.split(".")
        resource = None
        for key in keys:
            if not resource:
                resource = self.resources[key]
            else:
                resource = resource[key]

        if type(resource) != str:
            raise Exception("Attempting to return a non string attribute.")

        return resource
