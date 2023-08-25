import argparse
from .banner import *
from lib.organizations import print_organization_info
from lib.hunt_mail import Light, Basic
from lib.friends import output
from lib.user import trackx

async def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-u', '--username',
        nargs='?',
        type=str,
        default=None,
        help='searches all public information by username'
    )
    parser.add_argument(
        '-o', '--organization',
         nargs='?',
        type=str,
        default=None,
        help='searches all public information by organization'
    )
    parser.add_argument(
        '-e', '--email',
        nargs='?',
        type=str,
        default=None,
        help='search for an account by email'
    )
    parser.add_argument(
        '-f', '--friends',
        nargs='?',
        type=str,
        default=None,
        help='search for potential friends by username'
    )
    parser.add_argument(
        '-l', '--light',
        action='store_true',
        help="light mod with option '-e'"
    )

    args = parser.parse_args()

    if args.username:
        user = args.username
        print(banner)
        await trackx(user)
        exit()

    elif args.organization:
        org = args.organization
        print(banner)
        await print_organization_info(org)
        exit()

    elif args.light:
        if args.email:
            email = args.email
            print(banner)
            await Light.hunt(email)
            exit()

    elif args.email:
            print(banner)
            choice = input("\n[?] Do you want to log in? (y/n): ")
            if choice.lower() == "y":
                Basic.login()
            else:
                email = args.email
                await Basic.launch(email=email)
                exit()

    elif args.friends:
        username = args.friends
        print(banner)
        await output(user=username)
        exit()

    else:
        print(banner2)
        exit()
