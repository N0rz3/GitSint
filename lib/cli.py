import argparse
from lib.organizations import print_organization_info
from lib.hunt_mail import Hunt, Hunt_lightmod
from lib.friends import output
from lib.user import trackx
from lib.avatar import Avatar_Scraper
from lib.names_resembling import search
from .check_gitsint_version import Version

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
        help="light mode with option '-e'"
    )
    parser.add_argument(
        '-a', '--avatar',
        nargs='?',
        type=str,
        default=None,
        help='download profile picture (avatar) by username'
    )
    parser.add_argument(
        '-s', '--similar',
        nargs='?',
        type=str,
        default=None,
        help='search for similar names by usernamee'
    )
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help="check your version & update(s)"
    )

    args = parser.parse_args()

    if args.username:
        user = args.username
        await trackx(user)
        exit()

    elif args.organization:
        org = args.organization
        await print_organization_info(org)
        exit()

    elif args.light:
        if args.email:
            email = args.email
            await Hunt_lightmod.hunt(email)
            exit()

    elif args.email:
            email = args.email
            instance = Hunt(target=email)
            await instance.launch()
            exit()

    elif args.friends:
        username = args.friends
        await output(user=username)
        exit()

    elif args.avatar:
        u = args.avatar
        await Avatar_Scraper(name=u).downloader()
        exit()

    elif args.similar:
        username = args.similar
        await search(user=username)
        exit()

    elif args.version:
        await Version.check_update()

    else:
        exit(1)
