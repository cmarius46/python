from pythonping import ping


response_list = ping('', size = 40, count = 10)

print(response_list.rtt_avg, end = '\n')
print(response_list.rtt_avg_ms, end = '\n')


