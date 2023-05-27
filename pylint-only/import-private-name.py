from argparse import _AttributeHolder, _SubParsersAction  # [import-private-name]

attr_holder = _AttributeHolder()


def add_sub_parser(sub_parsers: _SubParsersAction) -> None:
    sub_parsers.add_parser("my_subparser")
    # ...
