import os
import yaml


def find_file_or_quit(fname):
    if not os.path.exists(fname):
        print("Cannot find %s" % fname)
        print("Are we in the right directory?")
        exit(-1)


def process(metadata_filename):
    find_file_or_quit(metadata_filename)
    with open(metadata_filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for old_name in data:
            record = data[old_name]
            sid = record[':submitters'][0][':sid']
            new_name = sid + '.pdf'
            print('renaming', old_name, 'to', new_name)
            find_file_or_quit(old_name)
            os.rename(old_name, new_name)


def main():
    metadata_filename = 'submission_metadata.yml'
    process(metadata_filename)


if __name__ == "__main__":
    main()
