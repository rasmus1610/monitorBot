import requests
import schedule
import time
import sendmail

urls = [
    ("http://mariusvach.de/", "grubert"),
    ("http://www.dr-grubert.de/", "vach"),
    ("http://www.zahnarzt-bernhard-datteln.de/", "vach"),
    ("http://physiotherapie-quante-benning.de/", "vach")
]


#1. make request to url

def job():

    successes = []
    failures = []
    
    for item in urls:
        r = requests.get(item[0])

        if item[1].lower() in r.text.lower():
            successes.append(item)
        else:
            sendmail.send_failure_message(item) #send email notification
            failures.append(item)

    if len(successes) > 0:
        print("=====SUCCESS=====")

        for item in successes:
            print("at {} everything is ok \n".format(item[0]))

    if len(failures) > 0:
        print("=====Failure=====")
        for item in failures:
            print("at '{}' the phrase '{}' is not found \n".format(item[0], item[1]))
    else:
        print("=====NO FAILURES=====")

schedule.every(1).hours.do(job)

if __name__ == "__main__":
    job()
    print("=====MONITORING STARTED=====")
    while True:
        schedule.run_pending()
        time.sleep(1)
