import datetime
def append_error_log( error_message ):
    Error_log_file = open("Error_log","a",encoding='utf8')
    Error_log_file.write( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + error_message + "\n" )
    Error_log_file.close()

