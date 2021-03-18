import auxiliaries as ax

# constants

DZIESIEC_KILO= 10000
MAX_LINES_TO_PARSE = 100*DZIESIEC_KILO
search_str ="Incorrect ETH share from GPU"
search_shares = "Eth: Incorrect shares "
error_table =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
shares_lost_in_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
config_file_name = "config.txt"

# functions

def traverse_log(file_name):

# open log
    log_file = ax.open_log_file(file_name)

# traverse log
    i = 1
    shares_lost = 0
    while i < MAX_LINES_TO_PARSE:

        line = log_file.readline()

        if line == "":
            break
        position_gpu = line.find(search_str) # localize the incorrect gpu
        position_shares = line.find((search_shares)) # localize the incorect shares

        if position_gpu != -1:
            print(i, position_gpu, line)
            gpu_no = int(line[position_gpu + len(search_str)])
            error_table[2][gpu_no - 1] += 1
        elif position_shares != -1:
            print(i, position_shares, line)
            share_no = ax.int_in_string(line,position_shares + len(search_shares))
            print("lost shares" + str(share_no))
            shares_lost += share_no
            shares_lost_in_time [ i // int(MAX_LINES_TO_PARSE/10)] += share_no
        if i % (MAX_LINES_TO_PARSE/10) == 0:
            print(i)
            i += 1
    ax.close_log_file(log_file)
    summary = """log file length in lines : {0}
                  : 1  2  3  4  5  6  7  8  9  10 11 12
    2 runs before :{1}
    1 runs before :{2}
    current run   :{3}
    
    All over shares lost: {4}
    {5}
    """.format(str(1), str(error_table[0]), str(error_table[1]), str(error_table[2]), str(shares_lost), str(shares_lost_in_time))

    return summary
