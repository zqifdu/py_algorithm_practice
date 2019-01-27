
# NOTE:
# - UTC timestamp in Python
# - Be more familiar with heapq function names

# Complexities:
# Space: O(n)
# Time: O(NlogN)

import heapq

#Minimun number of Meeting Rooms
def mininumNumberOfMeetingRooms(list_of_times):
    # edge case
    if not list_of_times:
        return 0
    # Parsing the time so it's a list of float pairs:
    time_slots = toNumericalPair(list_of_times)
    time_slots = sorted(time_slots)

    ending_heap = [time_slots[0][1]]

    for time_slot in time_slots[1:]:
        s, e = time_slot[0], time_slot[1]
        earliest_ending = ending_heap[0]
        if earliest_ending <= s:
            heapq.heappop(ending_heap)
            heapq.heappush(ending_heap, e)
        else:
            heapq.heappush(ending_heap, e)

    return len(ending_heap)

def toNumericalPair(list_of_times):
    numerical_list = []
    for time_str in list_of_times:
        start_num, end_num = timeToNumerical(time_str[0]), timeToNumerical(time_str[1])
        numerical_list.append(start_num, end_num)
    return numerical_lsit

def timeToNumerical(time_str):
    time_num = time_str.strip('amp')
    apm = time_str[-1:-3]
    time_num = [int(x) for x in time_num.split(':')]
    if len(time_num) == 2:
        time_num += time_num[1]*1.0/60
    time_num = time_num + 12 if apm == 'pm'
    return time_num

def minimumNumberOfMeetingRooms(list_of_times):
    # Pass the time so it's a list of float pairs:
    time_slots = toNumericalPair(list_of_times)

    # Sorting by the start time
    time_slots = sorted(time_slots)
    rooms = dict()
    num_rooms = 0
    # # TO OPTIMIZE: Maintain a heap to access the earliest ending time
    # earliest_ending = []
    for time in time_slots:
        if not rooms:
            # ending time of a room
            rooms[0] = time[1]
            num_rooms = 1
            # earliest_ending.append(time[1])
        else:
            # Choose a room that is available
            found_room = False
            for room_number in rooms:
                if rooms[room_number] < time[0]:
                    rooms[room_number] = max(time[1], rooms[room_number])
            if not found_room:
                rooms[num_rooms] = time[1]
                num_rooms += 1
            # if time[0] < earliest_ending[0]:
            #     heapy.push(earliest_ending, time[0])
    return num_rooms


def toNumericalPair(list_of_times):
    numerical_list = []
    for time in list_of_times:
        start_num = time[0].strip('apm')
        end_num = time[1].strip('apm')
        start_apm = time[0][-1:-3]
        end_apm = time[1][-1:-3]
        start_num = [int(x) for x in start_num.split(':')]
        start_num = start_num[0]
        if len(start_num) > 1:
            start_num += start_num[1]/60
        start_num
        # start = int(time[0][:-3]) + 12 if time[0][-1:-3] == 'pm' else 0
        # end = int(time[0][:-3]) + 12 if time[0][-1:-3] == 'pm' else 0
        numerical_list.append(start_num, end_num)
    return numerical_lsit
