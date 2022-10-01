class Animation:
    def __init__(self, frames, timeBetweenFrames):
        self.time = 0
        self.frameIndex = 0
        self.frame = frames[self.frameIndex]
        self.frames = frames
        self.speed = timeBetweenFrames

    def update(self, frameTime, entity):
        self.time += frameTime

        if(self.time >= self.speed):
            # update frame index
            self.frameIndex += 1
            if self.frameIndex >= len(self.frames):
                self.frameIndex = 0

            self.frame = self.frames[self.frameIndex]
            self.time = 0

        return self.frame

class PlayerIdleAnimation(Animation):
    def __init__(self, frames, timeBetweenFrames):
        super().__init__(frames, timeBetweenFrames)
        self.walk_anim = None

    def update(self, frameTime, entity):
        frame = super().update(frameTime, entity)
        if abs(entity.velocity[0]) + abs(entity.velocity[1]) > 0.01:
            #print("Walking!")
            entity.animator = self.walk_anim
        return frame

class PlayerWalkAnimation(Animation):
    def __init__(self, frames, timeBetweenFrames):
        super().__init__(frames, timeBetweenFrames)
        self.idle_anim = None

    def update(self, frameTime, entity):
        frame = super().update(frameTime, entity)
        if abs(entity.velocity[0]) + abs(entity.velocity[1]) < 0.01:
            entity.animator = self.idle_anim

        return frame
