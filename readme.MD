Bug on coverage:

python -m gevent.monkey --module pytest tests/ --cov=webapp --cov-report html -s

![](coverage_bug.jpg)



Works ok:

python -m pytest tests/ --cov=webapp --cov-report html -s


![](coverage_no_bug.jpg)
