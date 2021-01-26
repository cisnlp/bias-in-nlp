import argparse


def main(args):
    entries = []
    with open(args.input) as fp:
        next(fp)
        for line in fp:
            line = line.strip().split("\t")
            entry = {"title": line[0],
                     "paperlink": line[1],
                     "codelink": line[2],
                     "venue": line[4],
                     "year": int(line[4][-4:]),
                     "comment": line[6]}
            entries.append(entry)

    # sort and write
    entries = sorted(entries, key=lambda x: x["year"], reverse=True)

    entry_format = """
    **{title}**  
    {venue} - [Paper]({paperlink}), [Code]({codelink})  
    *Note:* {comment}
    """
    for entry in entries:
        to_add = entry_format.format(**entry)
        to_add = to_add.replace(", [Code]()", "")
        print(to_add)


if __name__ == '__main__':
    '''
    Usage:
    python update.py --input /Users/philipp/Downloads/Gender Bias Overview - RelatedWork.tsv >> output.md
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None, type=str, required=True, help="")
    args = parser.parse_args()
    main(args)
