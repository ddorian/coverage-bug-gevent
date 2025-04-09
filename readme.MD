Bug on coverage:

python -m gevent.monkey --module pytest tests/ --cov=webapp --cov-report html -s

![](coverage_bug.jpg)



Works ok with `--no-thread`:

python -m gevent.monkey --no-thread --module pytest tests/ --cov=webapp --cov-report html -s


![](coverage_no_bug.jpg)
