import pygame
import numpy as np
from pettingzoo.atari import space_invaders_v2

def play_space_invaders_realtime():
    # 1. Create the parallel environment
    env = space_invaders_v2.parallel_env(render_mode="human")
    env.reset()

    pygame.init()
    clock = pygame.time.Clock()

    # Track 'done' for both agents
    done = False

    # SPACE INVADERS (PettingZoo) has an action space of size 6 by default:
        #   0 = NOOP
        #   1 = FIRE
        #   3 = MOVE UP
        #   5 = MOVE RIGHT
        #   2 = MOVE LEFT
        #   4 = MOVE DOWN
        #
        # We'll map:
        #   Up arrow => action=2
        #   Down arrow => action=5
        #   Left arrow => action=3
        #   Right arrow => action=4
        #   Space => action=1
    key_map = {
        pygame.K_UP: 5,
        pygame.K_DOWN: 2,
        pygame.K_LEFT: 3,
        pygame.K_RIGHT: 4,
        pygame.K_SPACE: 1,
    }

    while not done:
        # 2. Poll keyboard events in pygame
        pygame.event.pump()
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Get a human-readable name for the key
                key_name = pygame.key.name(event.key)
                key = event.key
                #print(f"You pressed the '{key_name}' key.")
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    done = True

        # 3. Decide action for "first_0" (player) based on arrow keys + space
        action_first = 0  # default = NOOP
        if key in key_map:
            action_first = key_map[key]

        # 4. For "second_0", let's do no-op (you could also do random or another real player).
        action_second = 0

        # Create dict of actions: {'first_0': int, 'second_0': int}
        actions = {"first_0": action_first, "second_0": action_second}

        # 5. Step the environment
        obs, rewards, terminated, truncated, infos = env.step(actions)

        # Check if both agents are done
        if not terminated:
            print("Game is finished.")
            done = True

        # 6. Limit to ~30 FPS so it’s playable; adjust as needed
        clock.tick(30)

    env.close()
    pygame.quit()

if __name__ == "__main__":
    play_space_invaders_realtime()
