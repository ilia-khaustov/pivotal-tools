import urllib
import datetime
import sys
import argparse

import yaml
import requests

from pivotal_tools.client import PivotalClient
from pivotal_tools.reports import PivotalReportGenerator


if __name__ == '__main__':
    
    with open('config.yaml', 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--weeks-ago",
        type=int,
        help="0 for current week (default), 1 for previous and so on",
        default=0,
    )
    parser.add_argument(
        "--projects",
        type=int,
        nargs='*',
        help="Filter stories by project ids",
        default=[],
    )
    parser.add_argument(
        "--report",
        type=str,
        help="Report type",
        choices=['weekly_dev'],
        required=True,
    )
    args = parser.parse_args()

    pivotal_client = PivotalClient(
        tracker_token=config['pivotal']['tracker_token'],
        api_uri=config['pivotal']['api_uri'],
        projects=args.projects,
    )

    generator = PivotalReportGenerator(
        pivotal_client=pivotal_client
    )

    if not hasattr(generator, args.report):
        raise ValueError('Report type not found: {}'.format(args.report))

    report = getattr(generator, args.report)
    
    if not callable(report):
        raise ValueError('Report type not found: {}'.format(args.report))

    print(report())
