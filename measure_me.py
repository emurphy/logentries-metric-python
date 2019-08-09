from logentries import metrics
import os
import time

TEST = metrics.Metric(os.getenv("LOGENTRIES_TOKEN", "missing"))


@TEST.metric()
def function_one(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    function_one(1)