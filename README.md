# tail-follow-retry
Replacement for `tail --follow --retry` (or `tail -F`) in Python

## Why?

`tail -F` didn't work for us in an old CentOS Docker container which we used
for running test suites in Jenkins.

## Other similar Python implementations

- [python-inotify-tail_example](https://github.com/manos/python-inotify-tail_example)
  by Charlie Schluting ([@manos](https://github.com/manos))
