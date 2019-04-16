import json
from pprint import pprint
data = { "name":"inox", "seatInfo": { "A": { "numberOfSeats": 10, "aisleSeats": [0, 5 ,6, 9] }, "B": { "numberOfSeats": 15, "aisleSeats": [0, 5 ,6, 9] }, "D": { "numberOfSeats": 20, "aisleSeats": [0, 5 ,6, 9] } } }



def process(data):
	name = data['name']
	seat_info = data['seatInfo']

	seats = {}

	for row in seat_info:
		numberOfSeats = seat_info[row]['numberOfSeats']
		aisleSeats = seat_info[row]['aisleSeats']
		temp = []
		aisle_begin = True
		for i in range(numberOfSeats):
			if i in aisleSeats:
				if aisle_begin:
					temp.append(None)
					aisle_begin = False
				else:
					aisle_begin = True
			temp.append([i, True])
		last_aisle_seat = max(aisleSeats)
		last_aisle_seat_index = temp.index([last_aisle_seat, True])
		temp.insert(last_aisle_seat_index+1, None) # insert None to capture aisle property of last seat
		seats[row] = temp
	return seats
		
	# pprint(seats)
def find_seats(numSeats = 6, choice= 'A4'):
	seats = process(data)
	required_row = choice[0]
	required_seat = int(choice[1:])
	row = seats[required_row]
	first_potential_seat = required_seat - numSeats + 1
	first_potential_seat = max(first_potential_seat, 0)
	availableSeats = []
	result_found = False
	for i in range(first_potential_seat, required_seat):
		if [i, True] in row:
			starting_index = row.index([i, True])
			for seat in row[starting_index:numSeats+starting_index]:
				if seat and seat in row:
					availableSeats.append(seat[0])
				else:
					availableSeats = []
					break
		else:
			continue
		if len(availableSeats) == numSeats:
			result_found = True
			break
	if result_found:
		return { 'availableSeats': { required_row: availableSeats } }
	else:
		return { 'error' }




print(find_seats())