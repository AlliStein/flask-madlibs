"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

story = Story(
    ["noun1", "noun2", "adjective1", "adjective2", "noun3", "verb1", "noun4", "plural_noun", "noun5",
     "name", "verb2", "verb3", "adjective3", "place", "noun6"],
    """One {noun1}, down by the {noun2}, I found a(n) {adjective1} and {adjective2} {noun3}.  
        To my surprise, it could {verb1}!
        I sat with the {noun4} and we became {plural_noun}.  The {noun5}'s name is
        {name} and I {verb2} to {verb3} her at the {adjective3} {place} every {noun6}."""
)

# """One day, down by the river, I found an orange and blue turtle.  To my surprise, it could talk!
#       I sat with the turtle and we became friends.  The turtle's name is
#       Starlight and I go to visit her at the winding river every day."""
