from quote_bot.parser import ParsedMessage, Parser


class TestParseMessage:

    def assert_parsed_message(self, message: str, expected: ParsedMessage) -> None:
        parsed = Parser.parse(message)
        assert parsed is not None
        assert parsed.context == expected.context
        assert parsed.quote == expected.quote
        assert parsed.speaker == expected.speaker

    def test_spoiler_with_comma(self) -> None:
        message = '"Hello" - ||Sergio, in the morning||'
        self.assert_parsed_message(
            message,
            ParsedMessage(
                quote="Hello",
                speaker="Sergio",
                context="in the morning",
            ),
        )

    def test_spoiler_without_comma(self) -> None:
        message = '"Hello" - ||Sergio in the morning||'

        self.assert_parsed_message(
            message,
            ParsedMessage(
                quote="Hello",
                speaker="Sergio",
                context="in the morning",
            ),
        )

    def test_spoiler_with_spaced_comma(self) -> None:
        message = '"Hello" - ||Sergio ,in the morning||'
        self.assert_parsed_message(
            message,
            ParsedMessage(
                quote="Hello",
                speaker="Sergio",
                context="in the morning",
            ),
        )

    def test_quote_with_hyphen(self) -> None:
        message = '"Hello-There" - ||Sergio, in the morning||'
        self.assert_parsed_message(
            message,
            ParsedMessage(
                quote="Hello-There",
                speaker="Sergio",
                context="in the morning",
            ),
        )

    def test_spoiler_with_hyphen(self) -> None:
        message = '"Hello" - ||Sergio, in the early-morning||'
        self.assert_parsed_message(
            message,
            ParsedMessage(
                quote="Hello",
                speaker="Sergio",
                context="in the early-morning",
            ),
        )
