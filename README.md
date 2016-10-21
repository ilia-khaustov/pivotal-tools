# pivotal-tools

Set of useful tools for [Pivotal API](https://www.pivotaltracker.com/help/api)

## Install

This project requires python3.

You will need to install pip requirements first:

`pip3 install -r requirements.txt`

Second, copy sample config to a new file `config.yaml`:

`cp config.sample.yaml config.yaml`

Third, update your `config.yaml` with `pivotal.tracker_token` obtained from [Pivotal profile page](https://www.pivotaltracker.com/profile).

## Use

Entry point is the `cli.py` script.

### Arguments for `cli.py`

 * __required__ `--report` select report type, should be one of:
    * `weekly_dev` weekly report for developer
 * `--weeks-ago` use 0 for current week (default), 1 for previous and so on
 * `--projects` filter stories by projects using space-separated list of project ids

### Examples

Print developer report for current week:

`python3 cli.py --report weekly_dev` 

Print developer report for previous week:

`python3 cli.py --report weekly_dev --weeks-ago 1` 

Print developer report for current week for specified projects only:

`python3 cli.py --report weekly_dev --projects 2 3 5 8`