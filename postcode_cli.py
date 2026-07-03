"""A CLI application for interacting with the Postcode API."""


from argparse import ArgumentParser
from postcode_functions import validate_postcode, get_postcode_completions


def postcode_argparse():
    parser = ArgumentParser(
        description="Postcode CLI tool.")
    parser.add_argument(
        "--mode", "-m", help="Checks if a provided postcode is valid.", choices=["validate", "complete"], required=True)
    parser.add_argument(
        "postcode", help="Controls the numbers of results being displayed", default=5)
    args = parser.parse_args()
    return args.mode, args.postcode.strip().upper()


if __name__ == "__main__":
    mode, postcode = postcode_argparse()

    if mode == "validate":
        if validate_postcode(postcode):
            print(f"{postcode} is a valid postcode.")
        else:
            print(f"{postcode} is not a valid postcode.")

    elif mode == "complete":
        completions = get_postcode_completions(postcode)
        if completions == None:
            print(f"No matches for {postcode.upper().strip()}.")

        else:
            for completion in completions[:5]:
                print(completion)
