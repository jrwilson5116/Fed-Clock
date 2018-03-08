import random

def format_time(time):
    time = time.replace(":","")
    return int(time)


def get_minutes(formatted_time):
    minutes = formatted_time // 100 * 60
    minutes += formatted_time % 100
    return minutes


def get_time_decimal(clock_in,clock_out): 
    clock_in = format_time(clock_in)
    clock_out = format_time(clock_out)
    time_worked = get_minutes(clock_out) - get_minutes(clock_in)
    full_day = 510  
    if not time_worked % 6 == 0 and time_worked < full_day:
        time_worked += 5
    extraneous = time_worked % 6
    lunch_cutoff = 366
    if time_worked >= lunch_cutoff:
        extraneous += 30 
    time_worked -= extraneous
    decimal = time_worked // 60
    decimal += time_worked % 60 / 60
    return decimal 


def over_under(time):
    time *= 10
    time -= 80
    time /= 10
    return time


def main():
    print("#################################################")
    print("testing with random numbers")
    print("#################################################")
    for i in range(0,101):
        time_in = random.randint(6,12) * 100 + random.randint(0,60)
        time_out = random.randint(13,16) * 100 + random.randint(0,60)
        decimal = get_time_decimal(time_in,time_out)
        print("clocked in: "+str(time_in)+" clocked out: "+str(time_out)+ " decimal time: "+str(decimal)+" Over: "+str(over_under(decimal)))


if __name__ == "__main__":
    main()






