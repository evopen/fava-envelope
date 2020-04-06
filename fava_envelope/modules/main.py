import argparse
import logging
try:
    import ipdb
    #ipdb.set_trace()
except ImportError:
    pass

from beancount import loader

from fava_envelope.modules.beancount_envelope import BeancountEnvelope

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s: %(message)s')
    parser = argparse.ArgumentParser(description="beancount_envelope")
    parser.add_argument('filename', help='path to beancount journal file')
    args = parser.parse_args()

    # Read beancount input file
    entries, errors, options_map = loader.load_file(args.filename)
    ext = BeancountEnvelope(entries, options_map)
    df = ext.envelope_tables()
    #logging.info(df)
    print(df)


if __name__ == '__main__':
    main()
