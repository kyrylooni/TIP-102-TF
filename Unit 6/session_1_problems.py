# Standard Problem Set Version 1
# Problem 1: Building a Playlist

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:

    # Print out a nested Node assignment 

  

# 3. Translate each sub-problem into pseudocode:





# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
# print_linked_list(top_hits_2010s)


# Standard Problem Set Version 1
# Problem 1: Building a Playlist

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Should the function handle cases where the playlist is empty? If so, what should it return in such cases?
    # How should the function handle duplicate songs by the same artist? Should it count each occurrence separately or only unique songs?

# P - Plan
# 2. Write out in plain English what you want to do:
    # Initialize an empty dictionary to store the frequency of each artist:

    # This dictionary will have artist names as keys and their occurrence counts as values.
    # Start traversing the playlist from the head node:

    # Use a pointer (current) to iterate through the linked list.
    # For each song in the playlist:

    # Check if the artist is already in the dictionary:
    # If the artist is not in the dictionary, add them with a count of 1.
    # If the artist is already in the dictionary, increment their count by 1.
    # Move to the next node in the linked list:

    # Update the pointer to point to the next node.
    # Return the dictionary containing the frequency of each artist:

    # This dictionary will represent how many songs each artist has in the playlist.
   

  

# 3. Translate each sub-problem into pseudocode:
    # Initialize an empty dictionary to store the frequency of each artist:

    # artist_freq = {}
    # Start traversing the playlist from the head node:

    # current = playlist
    # While the current node exists:

    # Check if the artist of the current song is already in the dictionary:
    # If the artist is not in the dictionary:
    # Add the artist to the dictionary with a count of 1.
    # If the artist is already in the dictionary:
    # Increment the count for that artist by 1.
    # Move to the next node in the playlist:
    # current = current.next
    # Return the dictionary containing the frequency of each artist:

    # return artist_freq




# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    artist_freq = {}
    
    current = playlist
    
    while current:
          artist_freq[current.artist] = artist_freq.get(current.artist, 0) + 1 
          current = current.next
    
    return artist_freq


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))


# Problem 4: On Repeat

#U - Understand
# 1. Share 2 questions you would ask to help understand the question:


# P - Plan
# 2. Write out in plain English what you want to do:

    # Check if the playlist is empty:

    # If the playlist head is None, return False because there are no songs to check for a cycle.
    # Initialize two pointers:

    # A slow pointer that starts at the playlist head and moves one step at a time.
    # A fast pointer that also starts at the playlist head but moves two steps at a time.
    # Traverse the playlist using the slow and fast pointer technique:

    # While the fast pointer and its next node exist:
    # Move the slow pointer one step forward.
    # Move the fast pointer two steps forward.
    # Check if the slow pointer and fast pointer meet.
    # If the slow and fast pointers meet:

    # Return True, as this indicates a cycle exists in the playlist.
    # If the loop ends without the pointers meeting:

    # Return False, as this indicates there is no cycle in the playlist.

   

  

# 3. Translate each sub-problem into pseudocode:

    # Check if the playlist is empty:

    # If playlist_head is None, return False.
    # Initialize two pointers:

    # slow pointer starts at playlist_head.
    # fast pointer also starts at playlist_head.
    # Traverse the playlist using the slow and fast pointer technique:

    # While fast and fast.next exist:
    # Move the slow pointer one step forward: slow = slow.next.
    # Move the fast pointer two steps forward: fast = fast.next.next.
    # Check if the slow and fast pointers meet:

    # If slow == fast, a cycle exists in the playlist, so return True.
    # If the loop ends without the pointers meeting:

    # Return False, as there is no cycle in the playlist.



# I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    if not playlist_head:
        return False

    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next          
        fast = fast.next.next     

        if slow == fast:
            return True

    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))