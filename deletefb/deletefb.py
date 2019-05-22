#! /usr/bin/env python

import argparse
import getpass

from deletefb.tools.login import login
import deletefb.tools.wall as wall

def run_delete():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-E",
        "--email",
        required=True,
        dest="email",
        type=str,
        help="Your email address associated with the account"
    )

    parser.add_argument(
        "-P",
        "--password",
        required=False,
        dest="password",
        type=str,
        help="Your Facebook password"
    )

    parser.add_argument(
        "-U",
        "--profile-url",
        required=True,
        dest="profile_url",
        type=str,
        help="The link to your Facebook profile, e.g. https://www.facebook.com/your.name"
    )

    parser.add_argument(
        "-H",
        "--headless",
        action="store_true",
        dest="is_headless",
        default=False,
        help="Run browser in headless mode (no gui)"
    )

    args = parser.parse_args()

    args_user_password = args.password or getpass.getpass('Enter your password: ')

    driver = login(
        user_email_address=args.email,
        user_password=args_user_password,
        user_profile_url=args.profile_url,
        is_headless=args.is_headless
    )

    wall.delete_posts(driver)

if __name__ == "__main__":
    run_delete()
