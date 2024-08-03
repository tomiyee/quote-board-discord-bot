import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedMessage:
    """The results of parsing the content of a quote-board message"""

    quote: str
    """The content of the quote"""
    speaker: str
    """The name of the one who spoke the quote"""
    context: str | None
    """(optional) Any context accompanying the quote"""

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ParsedMessage):
            return False

        return (
            self.quote == value.quote
            and self.speaker == value.speaker
            and self.context == value.context
        )


class Parser:

    @classmethod
    def parse(cls, content: str) -> Optional[ParsedMessage]:
        """Parse the quote, speaker, and (optional) context from a Discord message"""

        parsed_quote = re.match(
            r"^\"(?P<quote>.*)\"\s*-\s*\|\|(?P<spoiler>.*?)\|\|$", content
        )

        if parsed_quote is None:
            return None

        spoiler = parsed_quote.group("spoiler")
        parsed_context = re.match(
            r"^(?P<speaker>\w+)((\s*,\s*)|(\s+))(?P<context>.*)", spoiler
        )

        if parsed_context is None:
            return None

        quote = parsed_quote.group("quote")
        speaker = parsed_context.group("speaker")
        context = parsed_context.group("context")

        return ParsedMessage(quote=quote, speaker=speaker, context=context)
