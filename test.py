from datetime import datetime


time_tmp = datetime.isoformat(datetime.now(), sep=' ', timespec='milliseconds')

    

print(time_tmp)