from celery import shared_task


@shared_task
def add(x, y):
    print("Done")
    return x + y