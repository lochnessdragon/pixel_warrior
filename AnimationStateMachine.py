class Animation:
    def __init__(self, frames, timeBetweenFrames):
        self.time = 0
        self.frameIndex = 0
        self.frame = frames[self.frameIndex]
        self.frames = frames
        self.speed = timeBetweenFrames

    def update(self, frameTime):
        self.time += frameTime

        if(self.time >= self.speed):
            # update frame index
            self.frameIndex += 1
            if self.frameIndex >= len(self.frames):
                self.frameIndex = 0

            self.frame = self.frames[self.frameIndex]
            self.time = 0

        return self.frame
