from celery import shared_task


@shared_task
def grading(submit_answer, answer):
    if submit_answer.text == answer.text:
        submit_answer.is_correct = True
        submit_answer.score = 100
        submit_answer.status = 2
    else:
        submit_answer.is_correct = False
        submit_answer.status = 2
    submit_answer.save()
