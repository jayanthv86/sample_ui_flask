__author__ = 'roymu_000'
import nfc
import nfc.ndef
import time
import uuid

def on_connect(tag):
    print(tag)


rdwr_options = {
    'on-connect': on_connect,
}

connected = False

def connect_reader(path):
    while True:
        try:
            return nfc.ContactlessFrontend(path)
        except IOError as error:
            time.sleep(0.5)
            continue

def write_tag(tag, tag_uid):
    if tag.ndef:
        sp = nfc.ndef.SmartPosterRecord("http://dell.com", tag_uid, action="save")
        print(sp.title)
        tag.ndef.message = nfc.ndef.Message(sp)
        return True

def main(tag_details, clf):
    while True:
        tag = clf.connect(rdwr=rdwr_options)
        if write_tag(tag, tag_details):
            print("Written")
            time.sleep(5)
            return

if __name__ == '__main__':
    main()