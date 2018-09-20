"Module reads local file for username/passwords"
def log_me_in_local(fname):
    with open(fname) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content
