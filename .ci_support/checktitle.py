import sys


if __name__ == "__main__":
    pr_title = sys.argv[1]
    with open("disableautomerge.txt", "r") as f:
        disable_lst = f.readlines()
    if len(pr_title) > 0:
        for disable in disable_lst:
            if len(disable.rstrip()) > 0 and disable.rstrip() in pr_title:
                sys.exit(1)
