import requests
import schedule
import time
import sendmail

urls = [
    ("http://mariusvach.de", "grubert"),
    ("http://dr-grubert.de", "vach"),
    ("http://zabd.de", "vach"),
    ("http://physiotherapie-quante-benning.de", "vach")
]

successes = []
failures = []

#1. make request to url

def job():

    for item in urls:
        r = requests.get(item[0])

        if item[1].lower() in r.text.lower():
            successes.append(item)
        else:
            sendmail.send_failure_message(item) #send email notification
            failures.append(item)

    if len(successes) > 0:
        print "=====SUCCESS====="

        for item in successes:
            print "at '%s' everything is ok \n" % item[0]

    if len(failures) > 0:
        print "=====Failure====="
        for item in failures:
            print "at '%s' the phrase '%s' is not found \n" % item
    else:
        print "=====NO FAILURES====="

schedule.every(12).hours.do(job)

if __name__ == "__main__":
    print "=====MONITORING STARTED====="
    while True:
        schedule.run_pending()
        time.sleep(1)
