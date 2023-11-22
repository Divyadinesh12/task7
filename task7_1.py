import datetime
curTime=datetime.datetime.now()
def create_file():
    with open("file_" + curTime.strftime("%Y_%m_%d_%H_%M_%S") +".txt","w") as file:
        file.write(curTime.strftime("%Y_%m_%d_%H_%M_%S"))
create_file()          