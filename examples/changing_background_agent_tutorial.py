import gym
import gym_urbandriving as uds
from gym_urbandriving.agents import KeyboardAgent, NullAgent, AccelAgent
from gym_urbandriving.state import SimpleIntersectionState
from gym_urbandriving.assets import Car, Pedestrian
from gym_urbandriving import UrbanDrivingEnv

def run():
    """
    Main function to be run to test simple_path_agent with hard coded path.

    Examples
    --------
    python3 examples/tree_search_train.py

    """

    vis = uds.PyGameVisualizer((800, 800))
    init_state = SimpleIntersectionState(ncars=3, nped=2)
    env = UrbanDrivingEnv(init_state=init_state,
                          visualizer=vis,
                          max_time=500,
                          randomize=True,
                          agent_mappings={Car:AccelAgent, 
                                          Pedestrian:AccelAgent},
                          )
    state = init_state
    env._render()

    agent = KeyboardAgent(agent_num=0)
    while (True):
       action = agent.eval_policy(state)
       state, reward, done, info_dict = env._step(action)
       env._render()

       if done:
          env._reset()
          state = env.get_state_copy()

run()
