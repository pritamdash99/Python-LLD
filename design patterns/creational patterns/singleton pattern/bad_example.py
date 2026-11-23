class Logger:
    def __init__(self, file_name : str) -> None:
        self.file_name = file_name
        self.log_count = 0

    def log(self, text : str):
        print(f"Logger is logging {text} in {self.file_name}")
        self.log_count += 1

#file 1 has log1 inside it to observe actions of file1
#file 2 has log2 inside it to observe actions of file2
#file 3 has log3 inside it to observe actions of file3

log1 = Logger("app.log")
log2 = Logger("app.log")
log3 = Logger("app.log")

#User 
log1.log("User is doing txn")

#Staff
log2.log("Staff is banning someone")

#Bank
log3.log("Bank is under service")

"""
Logger is logging User is doing txn in app.log
Logger is logging Staff is banning someone in app.log
Logger is logging Bank is under service in app.log
"""

print(log1.log_count, log2.log_count, log3.log_count)
# 1 1 1

# Even though the log file name is same in all 3 = "app.log"
# The count for each is 1 because these end up becoming new objects instead of incrementing the same log count.

print(id(log1), id(log2), id(log3))
# 2610380114304 2610379982480 2610379982800  they are all different addresses, object_ids.

# The goal is if the file name is same -> 
#   All logs produced should be 1 single object and the log count should increment.
# We do that using singleton pattern.
