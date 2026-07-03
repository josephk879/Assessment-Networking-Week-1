"""A CLI application for interacting with the Postcode API."""

"""#### Arguments
When run, the script should accept the following arguments:
1. `--mode`/`-m` : a **required** argument that accepts only the values `validate` and `complete`
2. `postcode` : a **required** argument that accepts a string

- `python3 postcode_cli.py --mode validate "FN1 MR2"`
- `python3 postcode_cli.py -m validate "FN3 XF5"`
- `python3 postcode_cli.py --mode complete "FN1"`
- `python3 postcode_cli.py -m complete "FN3"`

#### Validation mode
When the script is run and the `--mode`/`-m` argument has the value of `validate`, the tool should check if the 
provided postcode is valid.
If the postcode is valid, the tool should output `'[postcode] is a valid postcode.'` only.
If the postcode is not valid, the tool should output `'[postcode] is not a valid postcode.'` only.
Regardless of how they are entered, postcodes should be checked/displayed as **uppercase-only** strings with no trailing spaces.

#### Completion mode
When the script is run and the `--mode`/`-m` argument has the value of `complete`, the tool should display valid 
postcodes that would complete the provided partial postcode.
Each valid completion should be displayed on its own line, as shown below. A maximum of **5** possible completions should be shown.

```
TN12 0AA
TN12 0AB
TN12 0AD
TN12 0AE
TN12 0AF
```
If there are no valid completions, the tool should display only `'No matches for [postcode].'`"""


from argparse import ArgumentParser
def postcode_argparse() -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="Airport departure board")
    parser.add_argument(
        "--airport", help="Airport name to search for", required=True)
    parser.add_argument(
        "--export", "-e",
        help="Export to HTML, JSON, or both (default: both)",
        choices=["html", "json", "both"],
        default=None,
        required=False
    )
    args = parser.parse_args()
    return args.airport, args.export


if __name__ == "__main__":
    pass
