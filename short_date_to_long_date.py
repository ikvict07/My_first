# January, February, March, April, May, June, July,
# August, September, October, November, December;
# year, hour/hours, minute/minutes
"09.05.1945 06:30"


def date_time(time: str) -> str:
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    h = ['hour', 'hours']
    m = ['minute', 'minutes']
    splited = time.split()
    a, b, c = splited[0].split('.')
    e, f = splited[1].split(':')
    return f'{int(a)} {month[int(b)]-1} {int(c)} year ' + f'{int(e)} {h[0] if int(e) == 1 else h[1]} {int(f)} {m[0] if int(f) == 1 else m[1]}'


print(date_time("09.05.1945 06:30"))
