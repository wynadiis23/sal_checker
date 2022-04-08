import math

# calculate file size in KB, MB, GB
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.0f %s" % (math.ceil(size), x)
        size /= 1024.0


def devide_message(message, limit):
    chunks = [message[i:i+limit] for i in range(0, len(message), limit)]

    return chunks