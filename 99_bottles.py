count = 99;
def bottle_song():
	global count
	while (count < 100 and count > 1):
		print(f"{count} bottles of beer on the wall, {count} bottles of beer. Take one down and pass it around, {count - 1} bottles of beer on the wall.");
		count -= 1;
	if (count == 1):
		print('Take one down and pass it around, 1 bottle of beer on the wall. 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.');



bottle_song()
