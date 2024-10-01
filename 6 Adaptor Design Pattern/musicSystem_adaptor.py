# Step 1: Define the Old Music Player interface
class OldMusicPlayer:
    def play_cd(self, cd_name: str):
        raise NotImplementedError("This method should be overridden.")

# Step 2: Implement the Modern Music Player
class ModernMusicPlayer:
    def play_streaming(self, song_name: str):
        print(f"Playing {song_name} from a streaming service.")

# Step 3: Create an Adapter that adapts ModernMusicPlayer to OldMusicPlayer
class StreamingAdapter(OldMusicPlayer):
    def __init__(self, modern_player: ModernMusicPlayer):
        self.modern_player = modern_player

    def play_cd(self, cd_name: str):
        # Adapting the play_cd method to use the play_streaming method of ModernMusicPlayer
        print(f"Adapting CD '{cd_name}' to a streaming song.")
        self.modern_player.play_streaming(cd_name)

# Step 4: Client code demonstrating the Adapter Pattern
if __name__ == "__main__":
    # Create a modern music player
    modern_player = ModernMusicPlayer()

    # Use the adapter to connect the modern player to the old system
    adapter = StreamingAdapter(modern_player)

    # Now play a "CD" (which is really a streaming song)
    adapter.play_cd("Classic Hits")
