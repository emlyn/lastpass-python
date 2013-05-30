from lastpass import Fetcher, Parser
from getpass import getpass
from pprint import PrettyPrinter
import cPickle as pickle

if __name__ == "__main__":
    blob = None
    key = None
    username = raw_input("Username: ")
    password = getpass()
    if False:
        otp = raw_input("OTP (if rel): ")
        fetcher = Fetcher.fetch(username, password, otp=otp)
        key = fetcher.encryption_key
        blob = fetcher.blob
        pickle.dump(blob, open("blob.dat", "wb"))
    else:
        key = Fetcher.make_key(username, password)
        blob = pickle.load(open("blob.dat", "rb"))

    parser = Parser.parse(blob, key)

    equivdom = parser.chunks['EQDN']
    PrettyPrinter(indent=2).pprint(equivdom)
    accounts = parser.chunks['ACCT']
    PrettyPrinter(indent=2).pprint(accounts)
